#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, the strict_slashes ensures that
    the URL works both with or without the slash (/)
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Routing to root, the strict_slashes means the URL
    can work with or without the /
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Routing to C using variables"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """display "Python ", followed by the value of the text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Routing to n for integers only"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n=None):
    """Render HTML Page"""
    return render_template('5-number.html', name=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
