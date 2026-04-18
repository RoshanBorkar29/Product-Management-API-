from flask import jsonify, request
from service.models import Product

def read_product(product_id):
    product = Product.find(product_id)
    if not product:
        return {}, 404
    return jsonify(product.serialize()), 200


def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        return {}, 404

    data = request.get_json()
    product.name = data.get("name", product.name)
    product.update()

    return jsonify(product.serialize()), 200


def delete_product(product_id):
    product = Product.find(product_id)
    if not product:
        return {}, 404

    product.delete()
    return {}, 204


def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available:
        products = Product.find_by_availability(available.lower() == "true")
    else:
        products = Product.all()

    results = [p.serialize() for p in products]
    return jsonify(results), 200
