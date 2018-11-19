import datetime
from flask import session, request, jsonify
from app.function import *
from app import users, userIds, parcels, parcelIds, old_usernames
from werkzeug.security import generate_password_hash, check_password_hash


class User:
   # class to create users
    def __init__(self, username, email, password):
        if (username != '' and email != ''
                and password != '') or (username is not None
                                        and email is not None
                                        and password is not None):
            self.userId = len(users) + 1
            self.username = username
            self.email = email
            self.password_hash = self.create_a_password_for_a_user(password)

        else:
            raise ValueError('some arguments seem to be empty')

    def create_new_user(self):
        global users
        global old_usernames
        new_id = self.userId
        if self.username not in old_usernames:
            new_user = {}
            response = [self.username, self.password_hash, self.email]
            new_user[new_id] = response
            users.append(new_user)
            old_usernames.append(
                {'username': self.username, 'Id': self.userId})
        else:
            return json_response('message', 'failed to create your account.Try again')

    @staticmethod
    def create_a_password_for_a_user(password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(userId):
        for user in users:
            if userId in user.keys():
                return user[userId]

    @staticmethod
    def login(username, password):
        for username in old_usernames:
            if user['username'] == username:
                userId = user['Id']
                if check_password_hash(User.get_user(userId), password):
                    return True
                else:
                    return False

    @staticmethod
    def get_userId_by_username(username):
        for username in old_usernames:
            if user['username'] == username:
                userId = user['Id']
                return userId


    @staticmethod
    def logout():
        return True


class ParcelOrder:
    """ parcel class that creates a parcel for only a user that is registered """

    def __init__(self, userId, recipient, pickup_location, destination, description):
        if type(userId) == int and destination != '' and pickup_location != '' and recipient != '' and description != '':
            self.parcelId = len(parcels) + 1
            self.userId = userId
            self.date = datetime.datetime.utcnow()
            self.recipient = recipient
            self.pickup_location = pickup_location
            self.destination = destination
            self.description = description
            self.status = "Pending"
        else:
            raise ValueError('Some arguments seem to be empty')

    def create_parcel_order(self):
        # create a parcel
        global parcels
        global parcelIds
        new_parcel = {}
        new_id = self.userId
        response = [
            self.userId, self.recipient, self.pickup_location, self.destination,
            self.description, self.status
        ]
        new_parcel[new_id] = response
        parcels.append(new_parcel)
        return True

    @staticmethod
    def get_parcel_by_id(parcelId):
        # get  parcel by userId
        for parcel in parcels:
            if parcelId in parcel.keys():
                return parcel[parcelId]

    @staticmethod
    def modify_parcel(userId, parcelId, recipient='', pickup_location='', destination='', description=''):
        # authenticate that parcelId belongs to user
        global parcels

        if userId == ParcelOrder.get_parcel_by_id(parcelId)[0]:
            if recipient != '' and recipient != ParcelOrder.get_parcel_by_id(
                    parcelId)[1]:
                ParcelOrder.get_parcel_by_id(parcelId)[1] = recipient
            if pickup_location != '' and pickup_location != ParcelOrder.get_parcel_by_id(
                    parcelId)[2]:
                ParcelOrder.get_parcel_by_id(parcelId)[2] = pickup_location
            if destination != '' and destination != parcel.get_parcel_by_id(
                    parcelId)[3]:
                ParcelOrder.get_parcel_by_id(parcelId)[3] = destination
            if description != '' and description != ParcelOrder.get_parcel_by_id(
                    parcelId)[4]:
                ParcelOrder.get_parcel_by_id(parcelId)[4] = description
            return True

    @staticmethod
    def get_all_parcel_orders():
        # get  all registered parcels
        parcel_list = []
        for parcel in parcels:
            for key, value in parcel.items():
                parcel_list.append({
                    'Id': key,
                    'userId': value[0],
                    'recipient': value[1],
                    'pickup_location': value[2],
                    'destination': value[3],
                    'description': value[4]
                })
        return parcel_list

    @staticmethod
    def delete_parcel(userId, parcelId):
        # delete a parcel by userId if you are its owner
        global parcelIds
        global parcels
        if userId == ParcelOrder.get_parcel_by_id(Id)[0]:
            for parcel in parcels:
                if parcelId in parcel.keys():
                    parcels.remove(parcel)
                    parcelIds.remove(parcelId)
                    return True
        else:
            return False
