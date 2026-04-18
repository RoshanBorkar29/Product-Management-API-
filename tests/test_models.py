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
        
    def test_delete_a_product(self):
    """Test deleting a Product"""
    product = Product(
        name="Laptop",
        description="Gaming Laptop",
        price=1000.0,
        available=True,
        category="Electronics"
    )
    product.create()

    # Delete the product
    product.delete()

    deleted_product = Product.find(product.id)

    self.assertIsNone(deleted_product)

def test_list_all_products(self):
    """Test listing all Products"""
    Product(name="A", description="A", price=10, available=True, category="Cat1").create()
    Product(name="B", description="B", price=20, available=True, category="Cat2").create()

    products = Product.all()

    self.assertEqual(len(products), 2)
def test_find_by_name(self):
    """Test finding Product by name"""
    product = Product(name="Phone", description="Smartphone", price=500, available=True, category="Electronics")
    product.create()

    results = Product.find_by_name("Phone")

    self.assertTrue(len(results) > 0)
    self.assertEqual(results[0].name, "Phone")
def test_find_by_category(self):
    """Test finding Product by category"""
    product = Product(name="TV", description="LED", price=800, available=True, category="Electronics")
    product.create()

    results = Product.find_by_category("Electronics")

    self.assertTrue(len(results) > 0)
def test_find_by_availability(self):
    """Test finding Product by availability"""
    product = Product(name="Tablet", description="Android", price=300, available=True, category="Electronics")
    product.create()

    results = Product.find_by_availability(True)

    self.assertTrue(len(results) > 0)
