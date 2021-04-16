from flask import Flask, jsonify
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("D:/KJSCE/SEM 6/MSD/microservices/database/showtimes.json", "r") as f:
    showtimes = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>"
        }
    })


@app.route("/showtimes", methods=['GET'])
def showtimes_list():
    return jsonify(showtimes)


@app.route("/showtimes/<date>", methods=['GET'])
def showtimes_record(date):
    if date not in showtimes:
        raise NotFound
    print(showtimes[date])
    return jsonify(showtimes[date])

if __name__ == "__main__":
    app.run(port=5002, debug=True)
