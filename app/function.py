from flask import Flask, request, jsonify
from app import app

def json_response(title, message):
    json_message = {title: message}
    return jsonify(json_message)
