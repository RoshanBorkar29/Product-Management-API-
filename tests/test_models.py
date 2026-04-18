import unittest
from service.models import Product, db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        """Set up test database"""
        db.create_all()

    def tearDown(self):
        """Clean up database"""
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
        self.assertEqual(found_product.price, 1000.0)

    def test_update_a_product(self):
        """Test updating a Product"""
        product = Product(
            name="Laptop",
            description="Gaming Laptop",
            price=1000.0,
            available=True,
            category="Electronics"
        )
        product.create()

        # Update values
        product.name = "Updated Laptop"
        product.price = 1200.0
        product.available = False
        product.update()

        updated_product = Product.find(product.id)

        self.assertIsNotNone(updated_product)
        self.assertEqual(updated_product.name, "Updated Laptop")
        self.assertEqual(updated_product.price, 1200.0)
        self.assertEqual(updated_product.available, False)
