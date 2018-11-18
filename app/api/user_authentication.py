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
        """ checks token and creates a current_user object with users information"""
        token = None
        if 'access-token' in request.headers:
            token = request.headers['access-token']
        if not token:
            return json_response('message ', 'Unauthorized access! Token missing'), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.get_user(userId=data['Id'])
        except:
            return json_response('message', 'Token is invalid'), 401
        return f(current_user, *args, **kwargs)

    return decorated


