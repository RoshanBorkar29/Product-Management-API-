from behave import given
from service.models import Product

@given('the following products')
def step_impl(context):
    for row in context.table:
        product = Product(
            name=row['name'],
            description=row['description'],
            price=float(row['price']),
            available=row['available'] == "True",
            category=row['category']
        )
        product.create()
