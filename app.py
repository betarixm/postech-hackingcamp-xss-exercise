import urllib.parse

from flask import Flask, request, render_template
import os

from admin import checks_client_page

app = Flask(__name__)
app.secret_key = os.urandom(32)

PORT = int(os.getenv("APP_PORT", "8000"))


@app.route("/")
def index():
    word = request.args.get("word")
    is_correct = "correct" in request.args

    return render_template("index.html", word=word, is_correct=is_correct)


@app.route("/check", methods=["POST"])
def check():
    word = request.form["word"]

    if checks_client_page(word):
        return f'<script>alert("Good");location.href="/?word={urllib.parse.quote(word)}&correct";</script>'
    else:
        return f'<script>alert("Wrong");location.href="/?word={urllib.parse.quote(word)}&";</script>'


@app.route("/clear")
def clear():
    return '<script>localStorage.clear();location.href="/";</script>'


app.run(host="0.0.0.0", port=PORT, debug=False)
