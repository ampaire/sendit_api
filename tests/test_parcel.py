import json
import unittest

from flask import Flask, request
from api import app


class TestParcels(unittest.TestCase):
    def Setup(self):
        self.client = app.test_client()
        self.client.testing = True


    def test_delete(self):
        response = self.client.delete("/api/v1/parcels/1")
        self.assertEqual(response.status_code, 200)
        
    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/parcels/43")
        self.assertEqual(response.status_code, 404)
