import json
import unittest
from api.routes import *


class TestParcels(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_get_parcels(self):
        response = self.client.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete("/api/v1/parcels/1")
        self.assertEqual(response.status_code, 200)
        
    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/parcels/u")
        self.assertEqual(response.status_code, 404)

    

    
