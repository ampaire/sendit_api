from api import app
from api.models import *


@app.route("/")
def landing():
    return 'Welcome to sendIT. Happy browsing'


@app.route('/api/v1/parcels/<int:parcelId>', methods = ['DELETE'])
def cancel_a_delivery_order(parcelId):
    return delete_parcel()
