"""
This module provides a decorator to ensure that a user is logged in before accessing certain routes.
"""

from functools import wraps
from flask import session, jsonify


def login_required(f):
    """
    Decorator that checks if a user is logged in by verifying the presence of 'username' in the session.
    If the user is not logged in, it returns a JSON response with an error message and a 401 status code.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function
