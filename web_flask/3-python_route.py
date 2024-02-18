#!/usr/bin/python3
""" Add third view func that redirects and has default val for variable """

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route handler for the root URL ("/").

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the "/hbnb" URL.

    Returns:
        str: The string "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the "/c/<text>" URL.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The string "C " followed by the value of the text variable.
    """
    return 'C ' + escape(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler for the "/python/<text>" URL.

    Args:
        text (str, optional):  Text provided in the URL. Defaults to 'is cool'.

    Returns:
        str: The string "Python " followed by the value of the text variable.
    """
    return 'Python ' + escape(text.replace('_', ' '))


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
