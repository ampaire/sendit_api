from flask import Flask, request, jsonify
import datetime




parcels = []

def create_parcels():


    parcel = {
        "deliveryId": len(parcels)+1,
        "date": datetime.datetime.utcnow(),
        "location": request.get_json().get('location'),
        "destination": request.get_json().get('destination'),
        "weight": request.get_json().get('weight')
    }
    for parcel in parcels:
        if parcel in parcels:
            return jsonify({"message":"Oops! delivery order seems to exists"})
        if len(parcel) == 0:
            return jsonify({"message":"Cannot add empty parcel"})
    
    parcels.append(parcel)

    return jsonify({"parcels": parcels})

def get_parcel_orders():
    if len(parcels) < 1:
        return jsonify({'message': 'There is no data to display, add a delivery order'}), 400
    
        return jsonify({'parcels': parcels}), 200


def delete_parcel():
    parcel = [parcel for parcel in parcels if parcel['deliveryId'] == deliveryId]
    if len(parcel) == 0:
        return ("Failed to Delete! Cannot delete non-existent item")
    parcels.remove(parcel[0])
    return jsonify({'parcels': parcels, "message": 'Successfully Deleted'}), 200

