from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<username>', methods=['GET'])
def index(username):
    ret = "<h1> Hello, <em>" + username + "</em>!</h1>"
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2250)
