import json
from .base_test import BaseTestCase


class TestSales(BaseTestCase):

    def test_post_sales(self):
        """Only an attendant can post sales"""
        with self.client:
            # Register an attendant
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name="leticia",
                    email="ticia@gmail.com",
                    role="attendant",
                    username="ticia",
                    password="1234",
                    confirm_password="1234"
                )),
                content_type='application/json'
            )
            # Register admin
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name="leticia",
                    email="ticia@gmail.com",
                    role="admin",
                    username="ticia",
                    password="1234",
                    confirm_password="1234"
                )),
                content_type='application/json'
            )
            # login admin
            login_admin_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username="ticia",
                    password="1234"

                )),
                content_type='application/json'
            )

            # login the attendant
            login_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username="ticia",
                    password="1234"

                )),
                content_type='application/json'
            )

            # Test successful post of a sale
            response = self.client.post(
                '/api/v1/sales',
                data=json.dumps(dict(
                    items_count=4,
                    total_amount=5000
                )),
                content_type='application/json'
            )

            response_data = json.loads(response.data)
            self.assertEqual("A sale has been created successfully", response_data["message"])
            self.assertEqual(response.status_code, 201)

            # Test sale data can't be empty
            responsed = self.client.post(
                '/api/v1/sales',
                data=json.dumps(dict()
                                ),
                content_type='application/json'
            )
            response_datad = json.loads(responsed.data)
            self.assertEqual("Fields cannot be empty", response_datad["message"])
            self.assertEqual(responsed.status_code, 400)
            # Test some missing fields
            responsee = self.client.post(
                '/api/v1/sales',
                data=json.dumps(dict(
                    items_count="",
                    total_amount=5000
                )),
                content_type='application/json'
            )

            response_datae = json.loads(responsee.data)
            self.assertEqual("Items_count and total_amount fields can't be empty", response_datae["message"])
            self.assertEqual(responsee.status_code, 206)

    def test_get_all_sales(self):
        """Only an admin can view all sales records"""
        with self.client:
            # Register an attendant
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name="leticia",
                    email="ticia@gmail.com",
                    role="attendant",
                    username="ticia",
                    password="1234",
                    confirm_password="1234"
                )),
                content_type='application/json'
            )
            # Register admin
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name="leticia",
                    email="ticia@gmail.com",
                    role="admin",
                    username="ticia",
                    password="1234",
                    confirm_password="1234"
                )),
                content_type='application/json'
            )
            # login admin
            login_admin_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username="ticia",
                    password="1234"

                )),
                content_type='application/json'
            )

            # login the attendant
            login_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username="ticia",
                    password="1234"

                )),
                content_type='application/json'
            )

            # Test admin is not allowed to view all sales
            responseb = self.client.get('api/v1/sales')
            responseb_data = json.loads(responseb.data)
            self.assertEqual("Only an admin can view all sales records", responseb_data["message"])
            self.assertEqual(responseb.status_code, 401)
