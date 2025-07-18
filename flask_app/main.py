
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "A couple 100 internet documentations and I are Devops Engineers! lol<br>This is hosted on google cloud run... yaaaay!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("5000"), debug=True)
