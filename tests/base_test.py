from unittest import TestCase

from app import create_app


class BaseTestCase(TestCase):

    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """removes the dictionaries and the context"""
        self.app_context.pop()
