from flask import Flask, request, jsonify
from api.models import *
import datetime


parcels = [
    {   
        "parcelId": 1,
        "date": "Sun, 11 Nov 2018 14:15:53 GMT",
        "description": "Its a two kilogram package in a 1000cc box",
        "destination": "Kamwokya",
        "pickup_location": "Nyambya",
        "recipient": "kk",
        "status": "pending"
    }]


def create_parcel_delivery():
    for parcel in parcels:
        response = request.get_json()
        parcel_keys = list(response.keys())

        if 'pickup_location' not in parcel_keys:
            return jsonify({"message": "Cannot add parcel delivery with missing location"})
        if 'destination' not in parcel_keys:
            return jsonify({"message": "Cannot add parcel delivery with missing destination"})
        if 'recipient' not in parcel_keys:
            return jsonify({"message": "Provide the recipient"})
        if 'description' not in parcel_keys:
            return jsonify({"message": "We need to know the description of your package"})

        parcel = {
            "parcelId": parcels[-1]['parcelId']+1,
            "date": datetime.datetime.utcnow(),
            "pickup_location": response.get('pickup_location'),
            "destination": response.get('destination'),
            "recipient": response.get('recipient'),
            "description": response.get('description'),
            "status": response.get("status")
        }

        parcels.append(parcel)

        return jsonify({"message": 'Package added! Check all packages to confirm'})


def get_one_parcel(parcelId):
    parcel = [parcel for parcel in parcels if parcel["parcelId"] == parcelId]
    if len(parcel) == 0:
        return jsonify({"message": "Cannot find requested item"}), 400
    return jsonify({"parcel": parcel})


def get_parcel_orders():
    if len(parcels) < 1:
        return jsonify({'message': 'There is no data to display, add a delivery order'}), 400

    return jsonify({'parcels': parcels}), 200


def modify_delivery_order(parcelId):
    response = request.get_json()
    parcel = [parcel for parcel in delivery_orders if parcel["parcelId"] == parcelId]
    parcel[0]["location"] = response.get("location")
    parcel[0]["destination"] = response.get("destination")
    parcel[0]['recipient'] = response.get('recipient')
    parcel[0]["description"] = response.get("description")

    return jsonify({"message": "successfully modified"})


def delete_parcel(parcelId):
    parcel = [parcel for parcel in parcels if parcel['parcelId'] == parcelId]
    parcels.remove(parcel[1])
    return jsonify({"message": 'Successfully Deleted'}), 200
