from flask import Flask, request, jsonify
import datetime
from api import app

parcels = []




def delete_parcel():
    parcel = [parcel for parcel in parcels if parcel['deliveryId'] == deliveryId]
    if len(parcel) == 0:
        return ("Failed to Delete! Cannot delete non-existent item")
    parcels.remove(parcel[0])
    return jsonify({'parcels': parcels, "message": 'Successfully Deleted'}), 200
