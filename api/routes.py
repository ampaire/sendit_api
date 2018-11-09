from api.models import *

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key'

@app.route("/")
def landing():
    return 'Welcome to sendIT. Happy browsing'


@app.route('/api/v1/parcels', methods=['GET'])
def get_orders():
    return get_parcel_orders()


@app.route('/api/v1/parcels/<int:parcelId>', methods = ['DELETE'])
def cancel_a_delivery_order(parcelId):
    return delete_parcel()
