import jwt
import datetime
from flask import Flask
from functools import wraps
from app.models import User
from app.function import json_response

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwags):
        token = request.args.get('token')
        if not token:
            return json_response('message', 'the token is missing!')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            logged_in_user = User.get_user(userId)
        except:
            return json_response('message', 'Invalid token')
        return f(logged_in_user, *args, **kwags)
    return decorated


def user_login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': user.username}, app.config['SECRET_KEY'])

        return json_response('token',token)
    return ({"message": "Token is incorrect! "}), 401


