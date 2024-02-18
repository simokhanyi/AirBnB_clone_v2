#!/usr/bin/python3
""" Add fifth view func that displays HTML page if n is int """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display 'C ' followed by the value of the text variable."""
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display 'Python ' followed by value of the text variable."""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route to display '<n> is a number' if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route to display a HTML page with the number."""
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
