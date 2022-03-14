from flask import Flask, url_for, render_template, request, redirect
from os import system
from time import sleep
from hmac import new, compare_digest
from hashlib import sha256
from app_secrets import update_hash

app = Flask(__name__)


@app.before_request
def before_request():
    if app.env == "development":
        return
    if request.is_secure:
        return
    url = request.url.replace("http://", "https://", 1)
    code = 301
    return redirect(url, code=code)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/giftideas")
def giftideas():
    return render_template("gift_ideas.html")


@app.route("/update", methods=["POST"])
def update():
    sig_header = "X-Hub-Signature-256"
    if sig_header in request.headers:
        secret_hash = request.headers[sig_header].split("=")
        if len(secret_hash) == 2:
            req_sign = secret_hash[1]
            computed_sign = new(update_hash, request.data, sha256).hexdigest()
            if compare_digest(req_sign, computed_sign):
                threading.Thread(
                    target=lambda: [
                        sleep(2),
                        system("systemctl restart personalwebsite.service"),
                    ]
                ).start()
                return "update call successful"
    return "update call failed"


if __name__ == "__main__":
    app.run(debug=True)
