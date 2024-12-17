from flask import Blueprint, request
from methods.battery_type_manager import (
    create_battery_type,
    get_battery_type,
    get_all_battery_types,
    delete_battery_type
)
from logger_config import battery_type_logger

battery_type_blueprint = Blueprint('battery_type', __name__)

@battery_type_blueprint.route('/battery_type', methods=['POST'])
def create():
    battery_type_logger.info("POST /battery_type - Request to create a battery type.")
    battery_type_logger.debug(f"Request data: {request.get_json()}")
    response = create_battery_type()
    battery_type_logger.info("POST /battery_type - Response sent.")
    return response

@battery_type_blueprint.route('/battery_type/<int:id>', methods=['GET'])
def get(id):
    battery_type_logger.info(f"GET /battery_type/{id} - Request to fetch battery type with ID {id}.")
    response = get_battery_type(id)
    battery_type_logger.info(f"GET /battery_type/{id} - Response sent.")
    return response

@battery_type_blueprint.route('/battery_types', methods=['GET'])
def get_all():
    battery_type_logger.info("GET /battery_types - Request to fetch all battery types.")
    response = get_all_battery_types()
    battery_type_logger.info("GET /battery_types - Response sent.")
    return response

@battery_type_blueprint.route('/battery_type/<int:id>', methods=['DELETE'])
def delete(id):
    battery_type_logger.info(f"DELETE /battery_type/{id} - Request to delete battery type with ID {id}.")
    response = delete_battery_type(id)
    battery_type_logger.info(f"DELETE /battery_type/{id} - Response sent.")
    return response
