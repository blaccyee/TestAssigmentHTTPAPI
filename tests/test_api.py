from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app


class APITestCase(TestCase):
    """
    This a TestCase for our API application
    To run tests perform 'pytest tests'
    """

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # because we don't have a proper main page

    def test_create_product(self):
        # Actually for this test we need to have an isolated database to prevent strange values appears in your system
        json_data = {
            "product_form": {
                "product": "test_product",
                "category": "test_category"
            }
        }
        response = self.client.post('/create_product/', json=json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_store(self):
        response = self.client.get('/get_all_store/')
        self.assertEqual(response.status_code, 200)
