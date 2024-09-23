#!/usr/bin/python3
"""An interface to Flask Web Application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
# app.config['SERVER_NAME'] = "0.0.0.0:5000"


@app.route('/', strict_slashes=False)
def index():
    """Serve a request for a root directory"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Serve a request for /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    return "C {}".format(escape(text)).replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def coolPython(text=None):
    if not text:
        return "Python is cool"
    return "Python {}".format(escape(text)).replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
