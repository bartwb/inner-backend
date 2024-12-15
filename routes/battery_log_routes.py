from flask import Blueprint
from methods.battery_log_manager import (
    create_battery_log,
    get_battery_log,
    get_all_battery_logs,
    delete_battery_log
)

battery_log_blueprint = Blueprint('battery_log', __name__)

@battery_log_blueprint.route('/battery_log', methods=['POST'])
def create():
    return create_battery_log()

@battery_log_blueprint.route('/battery_log/<int:id>', methods=['GET'])
def get(id):
    return get_battery_log(id)

@battery_log_blueprint.route('/battery_logs', methods=['GET'])
def get_all():
    return get_all_battery_logs()

@battery_log_blueprint.route('/battery_log/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_battery_log(id)
