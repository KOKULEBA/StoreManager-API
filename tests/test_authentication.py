import json
from .base_test import BaseTestCase


class TestRegister(BaseTestCase):

    def test_registration(self):
        with self.client:
            """ Test successful registration """
            response = self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='leticia',
                    email='kokuleba@gmail.com',
                    role='attendant',
                    username='ticia',
                    password='password',
                    confirm_password='password'
                )),
                content_type='application/json'
            )
            response_data = json.loads(response.data)
            self.assertEqual("User with username ticia added successfully", response_data["message"])
            self.assertEqual(response.status_code, 201)

            """ Test registration using existing username """
            response1 = self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='leticia',
                    email='kokuleba@gmail.com',
                    role='attendant',
                    username='ticia',
                    password='password',
                    confirm_password='password'
                )),
                content_type='application/json'
            )
            response_data1 = json.loads(response1.data)
            self.assertEqual("Username already exists,try a different one!", response_data1["message"])

            """ Test registration with invalid email """
            response2 = self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='leticia',
                    email='kokulebagmail.com',
                    role='attendant',
                    username='ticia',
                    password='password',
                    confirm_password='password'
                )),
                content_type='application/json'
            )
            response_data2 = json.loads(response2.data)
            self.assertEqual("Enter a valid email address", response_data2["message"])
            self.assertEqual(response2.status_code, 403)

            """ test short password """
            result = self.client.post('/api/v1/auth/register',
                                      content_type="application/json",
                                      data=json.dumps({"name": "ticia", "username": "leticia",
                                                       "email": "leticia@gmail.com", "password": "123",
                                                       "confirm_password": "123", "role": "attendant"}))
            my_data = json.loads(result.data)
            self.assertEqual(result.status_code, 400)
            self.assertEqual("The password is too short,minimum length is 4", my_data["message"])

            """ test unmatching passwords """
            result2 = self.client.post('/api/v1/auth/register',
                                       content_type="application/json",
                                       data=json.dumps({"name": "Brenda", "username": "brenda",
                                                        "email": "brenda@co.com", "password": "Test123",
                                                        "confirm_password": "Test13", "role": "attendant"}))
            my_data2 = json.loads(result2.data)
            self.assertEqual(result2.status_code, 400)
            self.assertEqual("The passwords you entered don't match", my_data2["message"])

            """ test for missing fields """
            result3 = self.client.post('/api/v1/auth/register',
                                       content_type="application/json",
                                       data=json.dumps({"name": "", "username": "",
                                                        "email": "gebby@to.cm", "password": "Test123",
                                                        "confirm_password": "Test123", "role": "attendant"}))
            my_data3 = json.loads(result3.data)
            self.assertEqual(result3.status_code, 206)
            self.assertEqual("Make sure all fields have been filled out", my_data3["message"])

            """ Test for empty data """
            result4 = self.client.post('/api/v1/auth/register',
                                       content_type="application/json",
                                       data=json.dumps({}))
            my_data4 = json.loads(result4.data)
            self.assertEqual(result4.status_code, 400)
            self.assertEqual("Fields cannot be empty", my_data4["message"])

    def test_user_login(self):
        with self.client:
            """ Test for successful Login """
            response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='ticia',
                    password='password'

                )),
                content_type='application/json'
            )
            response_data = json.loads(response.data)
            self.assertEqual("Login successful!", response_data["message"])
            self.assertEqual(response.status_code, 200)

            """ Test for empty data """
            response2 = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict()
                                ),
                content_type='application/json'
            )
            response_data2 = json.loads(response2.data)
            self.assertEqual("Fields cannot be empty", response_data2["message"])
            self.assertEqual(response2.status_code, 400)

            """ Test for missing fields """
            response3 = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='',
                    password='1234'

                )),
                content_type='application/json'
            )
            response_data3 = json.loads(response3.data)
            self.assertEqual("Username or password missing", response_data3["message"])
            self.assertEqual(response3.status_code, 206)

            """ Test for invalid login """
            response4 = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='ticia',
                    password='1234567'

                )),
                content_type='application/json'
            )
            response_data4 = json.loads(response4.data)
            self.assertEqual("The password you entered is incorrect", response_data4["message"])

            """ Test for incorrect username """
            response5 = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='ruth',
                    password='1234'

                )),
                content_type='application/json'
            )
            response_data5 = json.loads(response5.data)
            self.assertEqual("Username does not exist in our records", response_data5["message"])
