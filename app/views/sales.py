import datetime
from flask import request, jsonify, Blueprint
from ..models import sales_model
from ..models.sales_model import SALES_DICT

sale = Blueprint('sale', __name__, url_prefix='/api/v1')

sale_object = sales_model.Sale()


@sale.route('/sales', methods=['POST'])
def post_sales():
    """Endpoint for only attendant to post a sale"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    item_count = data.get("items_count")
    total_amount = data.get("total_amount")
    created_by = "username"
    now = datetime.datetime.now()
    date_created = now
    sale_id = len(SALES_DICT)

    salesinfo = [item_count, total_amount]
    for i in salesinfo:
        if i is None or not i:
            return jsonify({"message": "Items_count and total_amount fields can't be empty"}), 206

    response = jsonify(sale_object.put(sale_id, date_created, created_by, item_count, total_amount))
    response.status_code = 201
    return response
