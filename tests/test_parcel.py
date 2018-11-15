import json
import unittest
from app.api.routes import *


class TestParcels(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True
        self.delivery_order = {
            "pickup_location": "kampala",
            "destination": "mbarara",
            "recipient": "Mr. Mugisha",
            "status": "Pending"
        }

    def test_can_add_delivery_order(self):
        response = self.client.post(
            "/api/v1/parcels", data=json.dumps(self.delivery_order), content_type="application/JSON")
        self.assertEqual(response.status_code, 201)

    def test_can_get_parcels(self):
        response = self.client.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)

    def test_can_get_one_parcel_delivery_order(self):
        response = self.client.get('/api/v1/parcels/1')
        self.assertEqual(response.status_code, 200)

    def test_cannot_get_non_existing(self):
        response = self.client.get('/api/v1/parcels/again')
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        response = self.client.delete("/api/v1/parcels/1")
        self.assertEqual(response.status_code, 200)

    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/parcels/u")
        self.assertEqual(response.status_code, 404)

    def test_invalid_JSON(self):
        response = self.client.post('/api/v1/parcels/1',
                                    data="This is a string!",
                                    content_type='application/json')
        self.assertEqual(response.status_code, 405)

    
