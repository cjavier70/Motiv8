from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
        body = "Welcome to Motiv8 API"
        return body


if __name__ == '__main__':
    app.run(debug=True)

