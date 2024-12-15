from flask import Blueprint
from methods.customer_type_manager import (
    create_customer_type,
    get_customer_type,
    get_all_customer_types,
    delete_customer_type
)

customer_type_blueprint = Blueprint('customer_type', __name__)

@customer_type_blueprint.route('/customer_type', methods=['POST'])
def create():
    return create_customer_type()

@customer_type_blueprint.route('/customer_type/<int:id>', methods=['GET'])
def get(id):
    return get_customer_type(id)

@customer_type_blueprint.route('/customer_types', methods=['GET'])
def get_all():
    return get_all_customer_types()

@customer_type_blueprint.route('/customer_type/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_customer_type(id)
