import unittest
from app.models import User
from app import users
from werkzeug.security import check_password_hash



class UserTestCase(unittest.TestCase):
    def setUpInstances(self):
        user = User('girl', 'girl@gmail.com', 'herpassword')
        return user

    def setUpInstances2(self):
        user2 = User('boy', 'boy@gmail.com', 'hispassword')
        return user2

    def test_class_instance(self):
        self.assertIsInstance(self.setUpInstances(), User)

    def test_no_user_has_been_created(self):
        self.assertEqual(len(users), 0)

    def test_username_is_not_similar_to_others(self):
        self.assertNotEqual(self.setUpInstances().username,
                            self.setUpInstances2().username)

    def test_created_user_cannot_be_empty(self):
        self.assertNotEqual(self.setUpInstances().username, '')
        self.assertNotEqual(self.setUpInstances().email, '')
        self.assertNotEqual(self.setUpInstances().password_hash, '')
        self.assertRaises(ValueError)

    def test_create_a_password_for_a_user_not_same_as_hashed_before(self):
        response = self.setUpInstances().create_a_password_for_a_user('herpassword')
        response2 = self.setUpInstances2().create_a_password_for_a_user('hispassword')
        self.assertNotEqual(response, response2)
        self.assertNotEqual(self.setUpInstances().password_hash, 'password')

    def test_verify_password(self):
        response = self.setUpInstances().verify_password('password')
        self.assertTrue(
            check_password_hash(self.setUpInstances().password_hash,
                                'herpassword'))
        self.assertFalse(
            check_password_hash(self.setUpInstances().password_hash, 'mine'))

    def test_logout(self):
        self.assertTrue(User.logout())
