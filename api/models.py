import datetime


class Users:
    users = []

    def __init__(self, name, email, password):
        if (username != '' and email != ''
                and password != '') or (username is not None
                                        and email is not None
                                        and password is not None):
            self.userId = userId
            self.name = name
            self.email = email
            self.password = password
        else:
            raise ValueError(
                "make sure the name, email and password fields are filled")


class Parcels:
    parcels = []

    def __init__(self, pickup_location, destination, recipient, description):
        if (pickup_location != '' and destination != ''
                and recipient != '' and description != "" and status != "") or (pickup_location is not None
                                                                                and destination is not None
                                                                                and recipient is not None
                                                                                and description is not None
                                                                                and status is not None):
        self. parcelId = parcelId
        self.pickup_location = pickup_location
        self.destination = destination
        self.recipient = recipient
        self.description = description
