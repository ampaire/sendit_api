import jwt
import datetime
from flask import Flask
from app.function import json_response

def required_with_token(f):
    @wraps(f)
    def decorated(*args, **kwags):
        token = request.args.get('token')
        if not token:
            return json_response('message', 'the token is missing!')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return json_response('message', 'Token is  invalid')

        return f(logged_in_user, *args, **kwags)

def user_login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': user.username}, app.config['SECRET_KEY'])

        return json_response('token',token)
    return ({"message": "Token is incorrect! "}), 401
