from flask import Blueprint, request
from methods.customer_manager import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
    get_customer_by_email
)
from logger_config import customer_logger

customer_blueprint = Blueprint('customer', __name__)

@customer_blueprint.route('/customer', methods=['POST'])
def create():
    customer_logger.info("POST /customer - Request to create a customer.")
    customer_logger.debug(f"Request data: {request.get_json()}")
    response = create_customer()
    customer_logger.info("POST /customer - Response sent.")
    return response

@customer_blueprint.route('/customer/<int:id>', methods=['GET'])
def get(id):
    customer_logger.info(f"GET /customer/{id} - Request to fetch customer with ID {id}.")
    response = get_customer(id)
    customer_logger.info(f"GET /customer/{id} - Response sent.")
    return response

@customer_blueprint.route('/customers', methods=['GET'])
def get_all():
    customer_logger.info("GET /customers - Request to fetch all customers.")
    response = get_all_customers()
    customer_logger.info("GET /customers - Response sent.")
    return response

@customer_blueprint.route('/customer/<int:id>', methods=['PUT'])
def update(id):
    customer_logger.info(f"PUT /customer/{id} - Request to update customer with ID {id}.")
    customer_logger.debug(f"Request data: {request.get_json()}")
    response = update_customer(id)
    customer_logger.info(f"PUT /customer/{id} - Response sent.")
    return response

@customer_blueprint.route('/customer/<int:id>', methods=['DELETE'])
def delete(id):
    customer_logger.info(f"DELETE /customer/{id} - Request to delete customer with ID {id}.")
    response = delete_customer(id)
    customer_logger.info(f"DELETE /customer/{id} - Response sent.")
    return response

@customer_blueprint.route('/customer/email/<email_address>', methods=['GET'])
def get_by_email(email_address):
    customer_logger.info(f"GET /customer/email/{email_address} - Request to fetch customer by email.")
    response = get_customer_by_email(email_address)
    customer_logger.info(f"GET /customer/email/{email_address} - Response sent.")
    return response
