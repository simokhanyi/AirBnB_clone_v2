#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello():
    """ returns HELLO HBNB"""
    return 'Hello HBNB!'

# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)