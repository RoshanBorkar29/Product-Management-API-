import unittest
from service.models import Product, db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_a_product(self):
        """Test reading a Product"""
        product = Product(
            name="Laptop",
            description="Gaming Laptop",
            price=1000.0,
            available=True,
            category="Electronics"
        )
        product.create()

        found_product = Product.find(product.id)

        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.name, "Laptop")
