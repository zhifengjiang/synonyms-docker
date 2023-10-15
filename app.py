from flask import Flask, request
import synonyms
import numpy as np  # Import numpy to help with the conversion

app = Flask(__name__)


@app.route("/nearby", methods=["GET"])
def nearby():
    word = request.args.get("word")
    if word:
        # Get the synonyms and their scores
        words, scores = synonyms.nearby(word)
        # Convert float32 to float
        scores = [float(score) for score in scores]
        return {"synonyms": list(zip(words, scores))}
    else:
        return {"error": "word parameter is required"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
