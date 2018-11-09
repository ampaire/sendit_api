from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key'