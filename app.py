from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/", methods=["GET", "POST"])
def home():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True, port=7000)
