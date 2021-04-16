from flask import Flask, jsonify
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("D:/KJSCE/SEM 6/MSD/microservices/database/movies.json", "r") as f:
    movies = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movies:
        raise NotFound

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return jsonify(result)


@app.route("/movies", methods=['GET'])
def movie_record():
    return jsonify(movies)


if __name__ == "__main__":
    app.run(port=5001, debug=True)

