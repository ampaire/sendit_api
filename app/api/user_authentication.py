import jwt
import datetime
from flask import Flask, request, jsonify, make_response
from functools import wraps
from app import *
from app.models import User
from app.function import json_response


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Access-token' in request.headers:
            token = request.headers['Access-token']
        else:
            return json_response('message', 'Token no longer valid, user signed out! Login again '), 401
        if not token:
            return json_response('message', 'Unauthorized access token is missing'), 401
        try:
            response = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.get_user(int(response['userId']))
        except:
            return json_response('message', 'Token is invalid'), 401
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/api/v1/auth/login', methods=['POST'])
def user_login():
    """ This logs in a registered user into system and creates a unique token for them"""
    
    response = request.get_json(force=True)
    user = {'username': self.username,
            'password': self.password}

    if len(response.keys()) != 2:
        return json_response("message", "Unknown user, register now or try to Login again"), 404


    token = jwt.encode({'username': user(username),
                        'exp': datetime.datetime.utcnow()
                        + datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"])

    return json_response('message', {'user_status': 'Successfully Logged in',
                                    'username': user.username, 'username': username,
                                    'token': token.decode('UTF-8')}), 200
