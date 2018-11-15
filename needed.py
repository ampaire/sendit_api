import jwt
import datetime


user = [{
    'name': 'effie',
    'password': 'unknown'
}]


@app.route("/login")

def login():
    return decorated
class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def log_in_required_with_token(f):
        @wraps(f)
        def decorated(*args, **kwags):
            token = request.args.get('token')
            if not token:
                return jsonify({'message': 'The token seems to be missing!'})
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
            except:
                return jsonify({'message': 'Token is  invalid'})

            return f(*args, **kwags)

    def user_login():
            auth = request.authorization
            if auth and auth.password == 'password':
                token = jwt.encode({'user': user.username}, app.config['SECRET_KEY'])

                return jsonify({'token': token})
            return make_response({"message": "Password is incorrect! "}), 401


 @app.route('/api/v1/parcels', methods= ['POST'])
# def create_order():
#     
def create_delivery(self):
    #     delivery_order = {
    #         "deliveryId": self.deliveryId,
    #         "date": self.date,
    #         "location": self.location,
    #         "destination": self.destination,
    #         "weight": self.weight
    #     }
    #     for delivery_order in delivery_orders:
    #         if len(delivery_order) == 0:
    #             return ("You have not added any delivery_order")
    #         if delivery_order['deliveryId'] == deliveryId:
    #             return ("Oops! delivery_order already exists")
            
    #         else:
    #             delivery_orders.append(delivery_order)

    #         return ({"delivery_orders": delivery_orders})


    ******************
    def get_delivery_orders():
    if len(delivery_orders) < 1:
        return jsonify({'message': 'There is no data to display, add a delivery order'}), 404

    else:
        return jsonify({'delivery_orders': delivery_orders}), 200
def create_delivery():


    delivery_order = {
        "deliveryId": len(delivery_orders)+1,
        "date": datetime.datetime.utcnow(),
        "location": request.get_json().get('location'),
        "destination": request.get_json().get('destination'),
        "weight": request.get_json().get('weight')
    }
    for delivery_order in delivery_orders:
        if delivery_order in delivery_orders:
            return jsonify({"message":"Oops! delivery order seems to exists"})
        if len(delivery_order) == 0:
            return jsonify({"message":"Cannot add empty delivery_order"})
    
    delivery_orders.append(delivery_order)

    return jsonify({"delivery_orders": delivery_orders})

def get_one_delivery_order():
   delivery_order = [delivery_order for delivery_order in entries if delivery_order["id_"] == id_]
    if len(delivery_order) ==0:
        abort(404)
    return jsonify({'delivery_order': delivery_order})
 

def modify_delivery_order():
    delivery_order = [delivery_order for delivery_order in delivery_orders if delivery_order["deliveryId"] == deliveryId]
    delivery_order[0]["location"] = request.get_json().get("location")
    delivery_order[0]["destination"] = request.get_json().get("destination")
    delivery_order[0]["weight"] = request.get_json().get("weight")

    return jsonify({"delivery_orders": delivery_orders})

    ******************
@app.route('/api/v1/parcels', methods=['GET'])
def get_orders():
    return get_delivery_orders()


@app.route('/api/v1/parcels', methods=['POST'])
def create_order():
    return create_delivery()


@app.route('/api/v1/parcels/<int:deliveryId>', methods=["PUT"])
def modify_a_delivery_order(deliveryId):
    return modify_a_delivery_order()