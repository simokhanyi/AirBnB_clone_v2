#!/usr/bin/python3
from flask import Flask

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


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
