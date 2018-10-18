import json
from .base_test import BaseTestCase


class TestProducts(BaseTestCase):

    def test_post_product(self):
        """Only an admin can post products"""
        with self.client:
            # Register an admin user
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='leticia',
                    email='kokuleba@gmail.com',
                    role='admin',
                    username='ticia',
                    password='password',
                    confirm_password='password'
                )),
                content_type='application/json'
            )
            # Register attendant
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='leticia',
                    email='kokuleba@gmail.com',
                    role='attendant',
                    username='leticia',
                    password='password',
                    confirm_password='password'
                )),
                content_type='application/json'
            )

            # login as admin
            login_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='ticia',
                    password='password'

                )),
                content_type='application/json'
            )
            result = json.loads(login_response.data)
            token = result

            # Login attendant
            login_att_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='leticia',
                    password='password'

                )),
                content_type='application/json'
            )
            resultatt = json.loads(login_att_response.data)
            tokenatt = resultatt
            # Test successful post
            response = self.client.post(
                '/api/v1/products',
                data=json.dumps(dict(
                    id=100,
                    name='chunky heels',
                    category='shoes',
                    purchase_price=1000,
                    selling_price=1800,
                    quantity=70,
                    low_limit=10,
                    description='A wide based heel'

                )),
                content_type='application/json'

            )

            response_data = json.loads(response.data)
            self.assertEqual("Product with id 100 added successfully", response_data["message"])
            self.assertEqual(response.status_code, 201)
            # Test post product with existing product id
            responsez = self.client.post(
                '/api/v1/products',
                data=json.dumps(dict(
                    id=100,
                    name='chunky heels',
                    category='shoes',
                    purchase_price=1000,
                    selling_price=1800,
                    quantity=70,
                    low_limit=10,
                    description='A wide based heel'

                )),
                content_type='application/json'

            )

            response_dataz = json.loads(responsez.data)
            self.assertEqual("The product Id you entered is being used for another product", response_dataz["message"])
            self.assertEqual(response.status_code, 201)

            # Test empty data
            response1 = self.client.post(
                '/api/v1/products',
                data=json.dumps(dict()
                                ),
                content_type='application/json'

            )
            response_data1 = json.loads(response1.data)
            self.assertEqual("Fields cannot be empty", response_data1["message"])
            self.assertEqual(response1.status_code, 400)
            # Test missing required fields
            response2 = self.client.post(
                '/api/v1/products',
                data=json.dumps(dict(
                    id="",
                    name="chunky",
                    category="shoes",
                    purchase_price=1000,
                    selling_price="",
                    quantity="",
                    low_limit="",
                    description="A wide based heel"

                )),
                content_type='application/json'

            )

            response_data2 = json.loads(response2.data)
            self.assertEqual("Some required fields are missing!", response_data2["message"])
            self.assertEqual(response2.status_code, 206)
            # Test only admin can post products
            responseatt_post = self.client.post(
                '/api/v1/products',
                data=json.dumps(dict(
                    id=200,
                    name='chunky heels',
                    category='shoes',
                    purchase_price=1000,
                    selling_price=1800,
                    quantity=70,
                    low_limit=10,
                    description='A wide based heel'

                )),
                content_type='application/json'

            )

            response_data_att = json.loads(responseatt_post.data)
            self.assertEqual("Product with id 200 added successfully", response_data_att["message"])
            self.assertEqual(responseatt_post.status_code, 201)


