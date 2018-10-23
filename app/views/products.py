from flask import request, jsonify, Blueprint

from ..models import product_model

product = Blueprint('product', __name__, url_prefix='/api/v1')

product_object = product_model.Product()


@product.route('/', methods=['GET'])
def index():
    """ root """
    if request.method == 'GET':
        # the following is a welcoming message (at the landing page)
        welcome_message = {"Message": [{
            "Welcome": "Hello! Welcome to Store manager"
        }]}

        response = {"status": "success", "Message": welcome_message}
        return response, 200


@product.route('/products', methods=['POST'])
def post_product():
    """Endpoint for only an admin to post a product"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    product_id = data.get("id")
    name = data.get("name")
    category = data.get("category")
    B_price = data.get("purchase_price")
    S_price = data.get("selling_price")
    qty = data.get("quantity")
    limit = data.get("low_limit")
    desc = data.get("description")

    productinfo = [product_id, name, qty, limit, S_price]
    for i in productinfo:
        if i is None or not i:
            return jsonify({"message": "Some required fields are missing!"}), 206
    response = jsonify(product_object.put(product_id, name, category, B_price, S_price, qty, limit, desc))

    response.status_code = 201
    return response


@product.route('/products', methods=['GET'])
def get_all_products():
    """Endpoint to get all products"""
    response = jsonify(product_object.get_all_products())
    response.status_code = 200
    return response


@product.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """Endpoint to get product by product id"""
    response = jsonify(product_object.get_product_by_id(product_id))
    response.status_code = 200
    return response
