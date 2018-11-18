from flask import Flask,session

"""variables that i will use throught"""
users = []
userIds = []
parcels = []
parcelIds = []
old_usernames = []


app = Flask(__name__)
app.config['SECRET_KEY'] = 'whocanguess'
