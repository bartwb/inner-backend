from flask import Blueprint
from methods.customer_manager import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
    get_customer_by_email
)

# Define the Blueprint
customer_blueprint = Blueprint('customer', __name__)

# Define routes
@customer_blueprint.route('/customer', methods=['POST'])
def create():
    return create_customer()

@customer_blueprint.route('/customer/<int:id>', methods=['GET'])
def get(id):
    return get_customer(id)

@customer_blueprint.route('/customers', methods=['GET'])
def get_all():
    return get_all_customers()

@customer_blueprint.route('/customer/<int:id>', methods=['PUT'])
def update(id):
    return update_customer(id)

@customer_blueprint.route('/customer/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_customer(id)

@customer_blueprint.route('/customer/email/<email_address>', methods=['GET'])
def get_by_email(email_address):
    return get_customer_by_email(email_address)
