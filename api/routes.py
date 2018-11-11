from api.controller import *

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key'

@app.route("/")
def landing():
    return 'Welcome to sendIT. Happy browsing'

@app.route("/users/<name>")
def welcome_message():
    return "Welcome %s ! How can we help you today?" %name

@app.route('/api/v1/parcels', methods=['POST'])
def create_order():
    return create_parcel_delivery()

@app.route('/api/v1/parcels/<int:parcelId>', methods = ['GET'])
def get_one_delivery_order(parcelId):
    return get_one_parcel(parcelId)


@app.route('/api/v1/parcels', methods=['GET'])
def get_orders():
    return get_parcel_orders()

@app.route('/api/v1/parcels/<int:parcelId>', methods = ['POST'])
def modify_delivery_order(parcelId):
    return modify_a_delivery_order(parcelId)


@app.route('/api/v1/parcels/<int:parcelId>', methods = ['DELETE'])
def cancel_a_delivery_order(parcelId):
    return delete_parcel('parcelId')
