from flask import Flask, request
import synonyms

app = Flask(__name__)


@app.route("/nearby", methods=["GET"])
def nearby():
    word = request.args.get("word")
    if word:
        words, _ = synonyms.nearby(
            word
        )  
        # Assuming synonyms.nearby returns a tuple of words and scores
        # Create a list of dictionaries with the word key
        synonyms_list = [{"word": word} for word in words]
        return {"synonyms": synonyms_list}
    else:
        return {"error": "word parameter is required"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
