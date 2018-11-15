from flask import Flask, request, session, jsonify
from app.models import *
from app.api.user_authentication import required_with_token
from app.function import json_response

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
                return json_response('message', 'Successfully created user ' + str(username)),201
            else:
                json_response('message', 'Failure creating user'), 400
        else:
            return json_response('message', 'Some fields are empty! '), 400
    else:
        return json_response(
            'message', 'Failed to create user, check to see whether the email, username and password fields are not empty'), 400


@app.route('/api/v1/auth/logout', methods=['POST'])
@required_with_token
def logout_user(logged_in_user):
    """This logs out user from the application"""
    request.authorization = None
    logged_in_user = None
    global users
    global userIds
    global percels
    global parcelIds
    global oldusers
    del users[:]
    del parcelIds[:]
    del percels[:]
    del oldusers[:]
    del userIds[:]
    if not request.authorization:
        return json_response('message', 'You have been successfully logout'), 200
    else:
        return json_response('message', 'Something went wrong, please try again '), 400



@app.route('/api/v1/parcels', methods=['POST'])
@required_with_token
def create_new_parcel_order(logged_in_user):
    """create new parcel order"""
    response = request.get_json()
    if response:
        if (len(response.keys()) == 4):
            userId = int(User.get_userId_by_username(logged_in_user[0]))
            pickup_location = response['pickup_location']
            destination = response['destination']
            recipient = response['recipient']
            description = response['description']
            parcel = parcel(userId, recipient, pickup_location, destination, description)
            if parcel:
                return json_response('message', 'Parcel order successfully created! Check all parcel orders to confirm'), 201
            else:
                return json_response('message','cannot create parcel with empty fields'), 400
    else:
        return json_response('message', 'Cannot create parcel! Some fields are empty'), 400


@app.route('/api/v1/parcels/<int:parcelId>', methods=['PUT'])
@required_with_token
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
        command = parcelOrder.modify_parcel(userId, parcelId, recipient, pickup_location,
                                          destination, description)
        if command:
            return json_response(
                'message', 'successfully updated parcel order ' + int(parcelId)), 201
        else:
            return json_response('message', 'Failed to update parcel order. Check to make sure you are logged in' + int(parcelId)), 400
    else:
        return json_response('message', 'parcel id does not exist'), 400


@app.route('/api/v1/parcels/<int:parcelId>', methods=['DELETE'])
@required_with_token
def delete_parcel_order(logged_in_user, parcelId):
    """delete parcel by id"""
    parcelId = int(parcelId)
    if parcelId in parcelIds:
        parcel_to_cancel = parcel.get_parcel_by_id(parcelId)
        userId = int(User.get_userId_by_username(logged_in_user[0]))
        command = parcel.delete_parcel_order(userId, parcelId)
        if command:
            return json_response('message','successfully deleted parcel delivery order' + int(parcelId)), 200
        else:
            return json_response('message', 'Failed to delete! Only user can delete the parcel order')
    else:
        return json_response('message', 'parcel id does not exist'), 404


@app.route('/api/v1/parcels', methods=['GET'])
@required_with_token
def get_all_parcel_orders(logged_in_user):
    """ retrieve all parcel_orders that were created"""
    if parcels:
        return jsonify('parcels', parcel.get_all_parcel_orders()), 200
    else:
        return json_response('message', 'No data to display. Create a delivery order'), 404