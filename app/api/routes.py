from flask import Flask, request, session, jsonify,make_response
from app.models import *
from app.api.user_authentication import token_required
from app.function import json_response
from app import users, userIds, parcelIds, parcels, old_usernames
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


@app.route('/')
def index():
    return '<h2> Welcome to sendIt. Happy browsing</h2>'

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    #route to login a user that has an account with the app
    auth = request.get_json()
    username = auth.get('username')
    password = auth.get('password')

    for user in users:
        if not username or not password:
            return json_response("message", "Could not verify username or password"), 401

        if (username == user['username'] and password == user['password']):
            token = create_access_token(identity={"userId":userIds,"username":username})

        return make_response('User Token', token), 200
    return json_response("message", "Could not verify! username and password dont match"), 401



@app.route('/api/v1/auth/signup', methods=['POST'])
def register_new_user():
    """route to sign up a new user to use the sendIt application"""

    response = request.get_json()
    if len(response.keys()) == 3:
        username = response['username']
        email = response['email']
        password = response['password']
        if (username is not None and email is not None and password is not None
            ) and (username != '' and email != ''
                   and password != ''):
            new_user = User(username, email, password)

            users.append(new_user.create_new_user())
            return json_response('message',users)
        else:
            return json_response('message', 'Some fields are empty! '), 400
    else:
        return json_response('message', 'Failed to create user, check to see whether the email, username and password fields are not empty'), 400


@app.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout_user(logged_in_user):
    request.authorization = None
    logged_in_user = None
    global users
    global userIds
    global parcels
    global parcelIds
    global usernames
    del users[:]
    del parcelIds[:]
    del parcels[:]
    del usernames[:]
    del userIds[:]
    if not request.authorization:
        return json_response('message', 'You have been successfully logout'), 200
    else:
        return json_response('message', 'Something went wrong, please try again '), 400



@app.route('/api/v1/parcels', methods=['POST'])
@jwt_required
def create_new_parcel_order(logged_in_user):
    """create new parcel order"""
    current_user = get_jwt_identity()
    response = request.get_json()
    if response:
        if (len(response.keys()) == 4):
            userId = current_user['userId']
            pickup_location = response['pickup_location']
            destination = response['destination']
            recipient = response['recipient']
            description = response['description']
            parcel = parcel_object.create_parcel_order(userId, recipient, pickup_location, destination, description)
            if parcel:
                return json_response('message', 'Parcel order successfully created! Check all parcel orders to confirm'), 201
            else:
                return json_response('message','cannot create parcel with empty fields'), 400
    else:
        return json_response('message', 'Cannot create parcel! Some fields are empty'), 400

@app.route('/api/v1/parcels', methods=['GET'])
@jwt_required
def get_all_parcel_orders(logged_in_user):
    """ get all parcel_orders that were created"""
    if parcels:
        return jsonify('parcels', parcel_object.get_all_parcel_orders()), 200
    else:
        return json_response('message', 'No data to display. Create a delivery order'), 404


@app.route('/api/v1/parcels/<int:parcelId>', methods=['PUT'])
@jwt_required
def modify_parcel_order(logged_in_user, parcelId):
    """update parcel"""
    if int(parcelId) in parcelIds and parcelId is not None:
        response = request.get_json()
        parcelId = int(parcelId)
        if 'recipient' in response.keys():
            recipient = response['recipient']
        else:
            recipient = ''
        if 'pickup_location' in response.keys():
            pickup_location = response['pickup_location']
        else:
            pickup_location = ''
        if 'destination' in response.keys():
            destination = response['destination']
        else:
            destination = ''
        if 'description' in response.keys():
            description = response['description']
        else:
            description = ''
        userId = int(User.get_userId_by_username(logged_in_user[0]))
        command = ParcelOrder.modify_parcel(userId, parcelId, recipient, pickup_location,
                                          destination, description)
        if command:
            return json_response(
                'message', 'successfully updated parcel order ' + int(parcelId)), 201
        else:
            return json_response('message', 'Failed to update parcel order. Check to make sure you are logged in' + int(parcelId)), 400
    else:
        return json_response('message', 'parcel id does not exist'), 400


@app.route('/api/v1/parcels/<int:parcelId>', methods=['DELETE'])
@jwt_required
def delete_parcel_order(logged_in_user, parcelId):
    """delete parcel by id"""
    parcelId = int(parcelId)
    if parcelId in parcelIds:
        parcel_to_cancel = ParcelOrder.get_parcel_by_id(parcelId)
        userId = int(User.get_userId_by_username(logged_in_user[0]))
        command = ParcelOrder.delete_parcel(userId, parcelId)
        if command:
            return json_response('message','successfully deleted parcel delivery order' + int(parcelId)), 200
        else:
            return json_response('message', 'Failed to delete! Only user can delete the parcel order')
    else:
return json_response('message', 'parcel id does not exist'), 404