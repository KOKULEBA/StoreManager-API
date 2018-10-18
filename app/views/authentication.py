"""auth_endpoints.py contains endpoints for register,login and logout"""
import re
from flask import request, jsonify, Blueprint
from ..models import authentication_models

authentication = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

user_object = authentication_models.Users()


@authentication.route('/register', methods=['POST'])
def register():
    """endpoint to add  a new user"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    username = data.get('username').strip()
    name = data.get('name')
    email = data.get('email').strip()
    password = data.get('password').strip()
    confirm_password = data.get('confirm_password').strip()
    role = data.get('role').strip()

    userinfo = [username, name, role, password, confirm_password, email]

    for i in userinfo:
        if i is None or not i:
            return jsonify({"message": "Make sure all fields have been filled out"}), 206
    if len(password) < 4:
        return jsonify({"message": "The password is too short,minimum length is 4"}), 400
    if confirm_password != password:
        return jsonify({"message": "The passwords you entered don't match"}), 400
    match = re.match(
        r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match is None:
        return jsonify({"message": "Enter a valid email address"}), 403
    response = jsonify(user_object.put(name, username, email, password, role))
    response.status_code = 201
    return response


@authentication.route('/login', methods=['POST'])
def login():
    """login user by verifying password and creating an access token"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Username or password missing"}), 206
    authorize = user_object.verify_password(username, password)
    response = jsonify(authorize)
    response.status_code = 401
    return response
