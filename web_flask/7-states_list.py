#!/usr/bin/python3
""" This script starts a Flask web application """
# import sys
# sys.path.append('~/AirBnB_clone_v2/models')
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def stateslist():
    all_states = storage.all(State).items()
    return (render_template('7-states_list.html', all_states=all_states))

@app.teardown_appcontext
def cleanup(exception):
    return (storage.close())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
