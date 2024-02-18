#!/usr/bin/python3
""" Script to start a Flask web application with 3 view functions """

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello():
    """
    Route handler for the root URL ("/").

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the "/hbnb" URL.

    Returns:
        str: The string "HBNB".
    """
    return 'HBNB'

# Route to display "C " followed by the value of the text variable
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


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
