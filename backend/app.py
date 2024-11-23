
"""
This module initializes and runs the Flask application.
"""

import os

from flask import Flask
from flask_session import Session

from db import init_db


app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure, randomly generated secret key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # Session expires after 30 mins
Session(app)

# Initialize the database
init_db()

from blueprints.auth import auth_bp 
app.register_blueprint(auth_bp)
