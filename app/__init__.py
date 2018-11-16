from flask import Flask,session
from flask_jwt_extended import JWTManager
"""variables that i will use throught"""
users = []
userIds = []
parcels = []
parcelIds = []
old_usernames = []


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardpassword'
app.config['JWT_SECRET_KEY'] = 'hardpassword'

jwt = JWTManager(app)
