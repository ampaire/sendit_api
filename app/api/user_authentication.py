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
        if not token:
            return json_response('message ','Token is missing'), 401
        try:
            response = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.get_user(userId= response['Id'])
        except:
            return json_response('message', 'Token is invalid'), 401
        return f(*args, **kwargs)

    return decorated



