#!/usr/bin/python3
""" Script that display 'C' and 'Python' """

from flask import Flask
from flask import render_template

app = Flask(__name__)


app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """Route to display 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>')
def c_text(text):
    """Route to display 'C ' followed by the value of the text variable."""
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_text(text):
    """Route to display 'Python ' followed by value of the text variable."""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n):
    """Route to display '<n> is a number' if n is an integer."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """Route to display a HTML page with the number."""
    return render_template('5-number.html', n=n)

# Running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
