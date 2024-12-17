from flask import Blueprint, request
from methods.customer_type_manager import (
    create_customer_type,
    get_customer_type,
    get_all_customer_types,
    delete_customer_type
)
from logger_config import customer_type_logger

customer_type_blueprint = Blueprint('customer_type', __name__)

@customer_type_blueprint.route('/customer_type', methods=['POST'])
def create():
    customer_type_logger.info("POST /customer_type - Request to create customer type.")
    customer_type_logger.debug(f"Request data: {request.get_json()}")
    response = create_customer_type()
    customer_type_logger.info("POST /customer_type - Response sent.")
    return response

@customer_type_blueprint.route('/customer_type/<int:id>', methods=['GET'])
def get(id):
    customer_type_logger.info(f"GET /customer_type/{id} - Request to fetch customer type with ID {id}.")
    response = get_customer_type(id)
    customer_type_logger.info(f"GET /customer_type/{id} - Response sent.")
    return response

@customer_type_blueprint.route('/customer_types', methods=['GET'])
def get_all():
    customer_type_logger.info("GET /customer_types - Request to fetch all customer types.")
    response = get_all_customer_types()
    customer_type_logger.info("GET /customer_types - Response sent.")
    return response

@customer_type_blueprint.route('/customer_type/<int:id>', methods=['DELETE'])
def delete(id):
    customer_type_logger.info(f"DELETE /customer_type/{id} - Request to delete customer type with ID {id}.")
    response = delete_customer_type(id)
    customer_type_logger.info(f"DELETE /customer_type/{id} - Response sent.")
    return response
