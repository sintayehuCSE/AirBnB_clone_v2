#!/usr/bin/python3
"""An interface to Flask Web Application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage


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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd(n):
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def close_app(func):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_state():
    return render_template("7-states_list.html", states=storage.all("State"))


@app.route("/cities_by_states", strict_slashes=False)
def cityOFStates():
    return render_template("8-cities_by_states.html",
                           states=storage.all("State"))


@app.route("/states", strict_slashes=False)
def states():
    return render_template("7-states_list.html", states=storage.all("State"))


@app.route("/states/<string:id>", strict_slashes=False)
def find_state_by_id(id):
    return render_template("9-states.html", states=storage.all("State"), id=id)


@app.route("/hbnb_alive", strict_slashes=False)
def hbnb_live():
    return render_template("100-hbnb.html", states=storage.all("State"), places=storage.all("Place"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
