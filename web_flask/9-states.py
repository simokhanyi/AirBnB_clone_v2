#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of states"""
    states = sorted(
            (storage.all("State").values(), key=lambda state: state.name))
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with cities of a state"""
    state = storage.get("State", id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
