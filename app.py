from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/giftideas")
def giftideas():
    return render_template("gift_ideas.html")


if __name__ == "__main__":
    app.run()
