from flask import Flask, request
import synonyms

app = Flask(__name__)


@app.route("/nearby", methods=["GET"])
def nearby():
    word = request.args.get("word")
    if word:
        words, _ = synonyms.nearby(
            word, 30
        )  # Assuming synonyms.nearby returns a tuple of words and scores
        # Filter out the query word and ensure only 20 synonyms are returned
        synonyms_list = [{"word": synonym} for synonym in words if synonym != word][:20]
        return {"synonyms": synonyms_list}
    else:
        return {"error": "word parameter is required"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
