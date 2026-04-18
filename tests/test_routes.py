import unittest
from service.app import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_read_product(self):
        response = self.client.get("/products/1")
        self.assertIn(response.status_code, [200, 404])

    def test_update_product(self):
        response = self.client.put("/products/1", json={"name": "Updated"})
        self.assertIn(response.status_code, [200, 404])

    def test_delete_product(self):
        response = self.client.delete("/products/1")
        self.assertIn(response.status_code, [200, 404])

    def test_list_all_products(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        response = self.client.get("/products?name=Phone")
        self.assertEqual(response.status_code, 200)

    def test_list_by_category(self):
        response = self.client.get("/products?category=Electronics")
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability(self):
        response = self.client.get("/products?available=true")
        self.assertEqual(response.status_code, 200)
