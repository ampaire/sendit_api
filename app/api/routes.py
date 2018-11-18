from flask import Flask, request, session, jsonify,make_response, url_for
from app.models import *
from app.api.user_authentication import token_required
from app.function import json_response
from functools import wraps
from app import users, userIds, parcelIds, parcels, old_usernames



@app.route('/')
def index():
    return '<h2> Welcome to sendIt. Happy browsing</h2>'


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
            user = User(username, email, password)

            if user:
                return json_response(
                    'message', str(username) + ' Your account has been created with SendIT'), 201
            else:
                json_response('message', 'Failed to create user'), 400
        else:
            return json_response('message', 'some fields seem to be empty or not set'), 400
    else:
        return json_response(
            'message', 'Could not create user, some fields missing'), 400

@app.route('/api/v1/auth/login', methods=['POST'])
def user_login():
    """ This logs in a registered user into system and creates a unique token for them"""
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp': datetime.datetime.utcnow()
                + datetime.timedelta(minutes= 30)}, app.config['SECRET_KEY'])

        return json_response('token', token.decode('UTF-8'))
    return json_response('message','Credentials do not match.Sign up instead')

@app.route('/api/v1/auth/logout', methods=['POST'])
@token_required
def logout_user(current_user):
    request.authorization = None
    current_user = None
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
@token_required
def create_new_parcel_order(current_user):
    """create new parcel order"""
    response = request.get_json()
    if response:
        if (len(response.keys()) == 4):
            userId =User.get_userId_by_username(current_user[0])
            pickup_location = response['pickup_location']
            destination = response['destination']
            recipient = response['recipient']
            description = response['description']
            parcel = ParcelOrder(userId, recipient, pickup_location, destination, description)
            if parcel:
                return json_response('message', 'Parcel order'+ int(parcelId)
                + ' successfully created! Check all parcel orders to confirm'), 201
            else:
                return json_response('message','cannot create parcel with empty fields'), 400
    else:
        return json_response('message', 'Cannot create parcel! Some fields are empty'), 400

@app.route('/api/v1/parcels', methods=['GET'])
@token_required
def get_all_parcel_orders(current_user):
    """ get all parcel_orders that were created"""
    if parcels:
        return jsonify('parcels', parcel_object.get_all_parcel_orders()), 200
    else:
        return json_response('message', 'No data to display. Create a delivery order'), 404


@app.route('/api/v1/parcels/<int:parcelId>', methods=['PUT'])
@token_required
def modify_parcel_order(current_user, parcelId):
    """update parcel"""
    if int(parcelId) in parcelIds and parcelId is not None:
        response = request.get_json()
        parcel_Id = int(parcelId)
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
        userId = int(User.get_userId_by_username(current_user[0]))
        command = ParcelOrder.modify_parcel(userId, parcel_Id, recipient, pickup_location,
                                          destination, description)
        if command:
            return json_response(
                'message', 'successfully updated parcel order ' + int(parcelId)), 201
        else:
            return json_response('message', 'Failed to update parcel order' + int(parcelId)), 400
    else:
        return json_response('message', 'parcel id does not exist'), 400


@app.route('/api/v1/parcels/<int:parcelId>', methods=['DELETE'])
@token_required
def delete_parcel_order(current_user, parcelId):
    """delete parcel by id"""
    parcel_Id = int(parcelId)
    if parcel_Id in parcelIds:
        parcel_to_delete = ParcelOrder.get_parcel_by_id(parcel_Id)
        userId = int(User.get_userId_by_username(current_user[0]))
        command = ParcelOrder.delete_parcel(userId, parcel_Id)
        if command:
            return json_response('message','successfully deleted parcel delivery order' + int(parcelId)), 200
        else:
            return json_response('message', 'Failed to delete! Try again later')
    else:
        return json_response('message', 'parcel id does not exist'), 404