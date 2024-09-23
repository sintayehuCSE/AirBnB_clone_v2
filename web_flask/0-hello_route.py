#!/usr/bin/python3
"""An interface to Flask Web Application"""
from flask import Flask


app = Flask(__name__)
app.config['SERVER_NAME'] = "0.0.0.0:5000"


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
