#!/usr/bin/python3
""" This script starts a Flask web application """
# import sys
# sys.path.append('~/AirBnB_clone_v2/models')
from flask import Flask, render_template
from sqlalchemy import text
from models import *
from models import storage
# from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def stateslist():
    all_state = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return (render_template('7-states_list.html', all_states=all_state))


@app.teardown_appcontext
def cleanup(exception):
    """ Closes the session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
