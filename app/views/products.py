from flask import request, jsonify, Blueprint,

from ..models import product_model

product = Blueprint('product', __name__,url_prefix='/api/v1')

product_object = product_model.Product()

@product.route('/products',methods=['POST'])
def post_product():
    """Endpoint for only an admin to post a product"""
    data=request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}),400
    product_id=data.get("id")
    name=data.get("name")
    category=data.get("category")
    B_price=data.get("purchase_price")
    S_price=data.get("selling_price")
    qty=data.get("quantity")
    limit=data.get("low_limit")
    desc=data.get("description")

    productinfo=[product_id,name,qty,limit,S_price]
    for i in productinfo:
        if i is None or not i:
            return jsonify({"message": "Some required fields are missing!"}) ,206
    response=jsonify(product_object.put(product_id, name, category, B_price,S_price,qty,limit,desc))

    response.status_code = 201
    return response
