from flask import Blueprint, request
from methods.battery_log_manager import (
    create_battery_log,
    get_battery_log,
    get_all_battery_logs,
    delete_battery_log
)
from logger_config import battery_log_logger  # Use the existing logger

battery_log_blueprint = Blueprint('battery_log', __name__)

@battery_log_blueprint.route('/battery_log', methods=['POST'])
def create():
    battery_log_logger.info("POST /battery_log - Request to create a battery log.")
    battery_log_logger.debug(f"Request data: {request.get_json()}")
    response = create_battery_log()
    battery_log_logger.info("POST /battery_log - Response sent.")
    return response

@battery_log_blueprint.route('/battery_log/<int:id>', methods=['GET'])
def get(id):
    battery_log_logger.info(f"GET /battery_log/{id} - Request to retrieve battery log with ID {id}.")
    response = get_battery_log(id)
    battery_log_logger.info(f"GET /battery_log/{id} - Response sent.")
    return response

@battery_log_blueprint.route('/battery_logs', methods=['GET'])
def get_all():
    battery_log_logger.info("GET /battery_logs - Request to retrieve all battery logs.")
    response = get_all_battery_logs()
    battery_log_logger.info("GET /battery_logs - Response sent.")
    return response

@battery_log_blueprint.route('/battery_log/<int:id>', methods=['DELETE'])
def delete(id):
    battery_log_logger.info(f"DELETE /battery_log/{id} - Request to delete battery log with ID {id}.")
    response = delete_battery_log(id)
    battery_log_logger.info(f"DELETE /battery_log/{id} - Response sent.")
    return response
