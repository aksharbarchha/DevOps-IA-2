from flask import Flask, jsonify
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("D:/KJSCE/SEM 6/MSD/microservices/database/bookings.json", "r") as f:
    bookings = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "uri": "/",
        "subresource_uris": {
            "bookings": "/bookings",
            "booking": "/bookings/<username>"
        }
    })


@app.route("/bookings", methods=['GET'])
def booking_list():
    return jsonify(bookings)


@app.route("/bookings/<username>", methods=['GET'])
def booking_record(username):
    if username not in bookings:
        raise NotFound

    return jsonify(bookings[username])

if __name__ == "__main__":
    app.run(port=5003, debug=True)

