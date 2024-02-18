#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Route to display 'C' followed by the value of the text variable.

    Args:
        text (str): The text variable extracted from the URL.

    Returns:
        str: Concatenation of 'C'.
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Route to display 'Python' followed by the value of the text variable.

    Args:
        text (str): The text variable from the URL (default is 'is cool').
    Returns:
        str: Concatenation of 'Python'.
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display '<n> is a number' if n is an integer.

    Args:
        n (int): The integer variable extracted from the URL.

    Returns:
        str: A string indicating whether n is a number or not.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display an HTML page if n is an integer.

    Args:
        n (int): The integer variable extracted from the URL.

    Returns:
        str: An HTML page with "Number: n" inside the <h1> tag of the body.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to display an HTML page indicating if n is odd or even.

    Args:
        n (int): The integer variable extracted from the URL.

    Returns:
        str: An HTML page inside the <h1> tag of the body.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
