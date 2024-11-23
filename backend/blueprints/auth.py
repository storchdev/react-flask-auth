"""
This module provides authentication routes for the backend.
"""

from flask import Blueprint, session, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from db import query_db
from checks import login_required


auth_bp = Blueprint("auth", __name__, url_prefix="/")


@auth_bp.route('/api/auth-check', methods=["GET"])
def auth_check():
    """
    Check if the user is authenticated based on the session.
    Returns:
        Response: A JSON response with status "authenticated" and HTTP status code 200 if the user is authenticated.
                  A JSON response with an error message "Unauthorized" and HTTP status code 401 if the user is not authenticated.
    """

    if 'username' in session:
        return jsonify({"status": "authenticated"}), 200
    return jsonify({"error": "Unauthorized"}), 401


# Register endpoint
@auth_bp.route('/api/register', methods=['POST'])
def register():
    """
    Registers a new user.

    This function handles the registration of a new user by accepting a JSON payload
    containing a username and password. It performs validation to ensure both fields
    are provided and checks if the username already exists in the database. If the
    username is unique, it hashes the password and inserts the new user into the database.

    Returns:
        Response: A JSON response indicating the result of the registration process.
        - 201: User registered successfully.
        - 400: Username and password are required, or user already exists.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = query_db("SELECT * FROM users WHERE username = ?", (username,), one=True)
    if user:
        return jsonify({"error": "User already exists"}), 400

    password_hash = generate_password_hash(password)
    query_db("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))

    return jsonify({"message": "User registered successfully"}), 201

# Login endpoint
@auth_bp.route('/api/login', methods=['POST'])
def login():
    """
    Handle user login.

    This function retrieves the username and password from the request's JSON payload,
    validates them, and checks the credentials against the database. If the credentials
    are valid, it sets the session for the user and returns a success message. Otherwise,
    it returns an error message.

    Returns:
        Response: A JSON response with a success message and status code 200 if the login
        is successful, or an error message and status code 400/401 if the login fails.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = query_db("SELECT * FROM users WHERE username = ?", (username,), one=True)
    if user and check_password_hash(user['password_hash'], password):
        session['username'] = username  # Set session
        session.permanent = True
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Home endpoint (protected)
@auth_bp.route('/api/home', methods=['GET'])
@login_required
def home():
    """
    Handle the home route for the authentication system.

    The @login_required is used to ensure the user is authenticated.

    Returns:
        Response: A Flask JSON response with either an error message and 401 status code,
                  or a welcome message and 200 status code.
    """
    return jsonify({"message": f"Welcome, {session['username']}!"}), 200

# Logout endpoint
@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    """
    Logs out the current user by removing the 'username' from the session.

    Returns:
        tuple: A JSON response indicating successful logout and an HTTP status code 200.
    """
    session.pop('username', None)
    return jsonify({"message": "Logged out successfully"}), 200
