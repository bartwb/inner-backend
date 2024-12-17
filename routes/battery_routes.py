from flask import Blueprint, request
from methods.battery_manager import (
    create_battery,
    get_battery,
    get_all_batteries,
    update_battery,
    delete_battery
)
from logger_config import battery_logger  # Import your battery logger

battery_blueprint = Blueprint('battery', __name__)

@battery_blueprint.route('/battery', methods=['POST'])
def create():
    battery_logger.info("POST /battery - Request to create a new battery.")
    battery_logger.debug(f"Request data: {request.get_json()}")
    response = create_battery()
    battery_logger.info("POST /battery - Response sent.")
    return response

@battery_blueprint.route('/battery/<int:id>', methods=['GET'])
def get(id):
    battery_logger.info(f"GET /battery/{id} - Request to fetch battery with ID {id}.")
    response = get_battery(id)
    battery_logger.info(f"GET /battery/{id} - Response sent.")
    return response

@battery_blueprint.route('/batteries', methods=['GET'])
def get_all():
    battery_logger.info("GET /batteries - Request to fetch all batteries.")
    response = get_all_batteries()
    battery_logger.info("GET /batteries - Response sent.")
    return response

@battery_blueprint.route('/battery/<int:id>', methods=['PUT'])
def update(id):
    battery_logger.info(f"PUT /battery/{id} - Request to update battery with ID {id}.")
    battery_logger.debug(f"Request data: {request.get_json()}")
    response = update_battery(id)
    battery_logger.info(f"PUT /battery/{id} - Response sent.")
    return response

@battery_blueprint.route('/battery/<int:id>', methods=['DELETE'])
def delete(id):
    battery_logger.info(f"DELETE /battery/{id} - Request to delete battery with ID {id}.")
    response = delete_battery(id)
    battery_logger.info(f"DELETE /battery/{id} - Response sent.")
    return response
