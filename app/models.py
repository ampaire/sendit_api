from flask import session, request, jsonify
from app.function import *
from app import users, userIds, parcels, parcelIds, old_usernames
from werkzeug.security import generate_password_hash, check_password_hash
 

class User:
   #class to create users 
    def __init__(self, username, email, password):
        if (username != '' and email != ''
                and password != '') or (username is not None
                                        and email is not None
                                        and password is not None):
            self.userId = len(users) +1
            self.username = username
            self.email = email
            self.password_hash = self.create_a_password_for_a_user(password)
            self.create_new_user()
        else:
            raise ValueError ('some arguments seem to be empty')
   

    def create_new_user(self):
        global users
        global old_usernames
        new_id = self.userId
        if self.username not in old_usernames:
            new_user = {}
            response = [self.username, self.password_hash, self.email]
            new_user[new_id] = response
            users.append(new_user)
            old_usernames.append({'username': self.username, 'userId': self.userId})
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
            else:
                return json_response('message','User does not seem to exist')

    @staticmethod
    def login(username, password):
        for olduser in old_usernames:
            if olduser['username'] == username:
                userId = olduser['Id']
                if check_password_hash(User.get_user(userId)[1], password):
                    return True
                else:
                    return False
            else:
                return json_response('message', 'Check to make sure your login details are matching')


    @staticmethod
    def get_userId_by_username(username):
        for olduser in usernames:
            if olduser['username'] == username:
                userId = olduser['userId']
                return userId

class ParcelOrder:
    """ parcel class that creates a parcel for only a user that is registered """

    def __init__(self, userId, recipient, pickup_location, destination, description):
        if type(userId) == int and destination != '' and pickup_location != '' and  recipient!= '' and description != '':
            self.parcelId = generate_parcel_id()
            self.userId = userId
            self.date = creation_date()
            self.price = generate_price()
            self.recipient = recipient
            self.pickup_location = pickup_location
            self.destination = destination
            self.description = description
            self.status = "Pending"
            self.create_parcel_delivery_order()

        else:
            raise ValueError('Some arguments seem to be empty')

    def creation_date(self):
        date_of_parcel_creation = datetime.datetime.utcnow()
        return date_of_parcel_creation()

    def generate_business_id(self):
        # generates a business id
        global parcelIds
        new_id = generate_random_number()
        if new_id not in parcelIds:
            parcelIds.append(new_id)
            return new_id
        else:
            self.generate_business_id()

    def generate_price(self):
        pass
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
        global parcels
        if userId == parcel.get_parcel_by_id(parcelId)[0]:
            for parcel in parcels:
                if parcelId in parcel.keys():
                    parcels.remove(parcel)
                    parcelIds.remove(parcelId)
                    return True
        else:
            return False

