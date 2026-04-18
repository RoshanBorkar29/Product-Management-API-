from factory import Factory, Faker
from service.models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product

    name = Faker('word')
    description = Faker('sentence')
    price = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    available = Faker('boolean')
    category = Faker('word')
