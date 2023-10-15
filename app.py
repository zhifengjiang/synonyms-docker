from flask import Flask, request
import synonym

app = Flask(__name__)


@app.route("/nearby", methods=["GET"])
def nearby():
    word = request.args.get("word")
    if word:
        synonyms = synonym.nearby(word)
        return {"synonyms": synonyms}
    else:
        return {"error": "word parameter is required"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
