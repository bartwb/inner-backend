from flask import Blueprint
from methods.battery_type_manager import (
    create_battery_type,
    get_battery_type,
    get_all_battery_types,
    delete_battery_type
)

battery_type_blueprint = Blueprint('battery_type', __name__)

@battery_type_blueprint.route('/battery_type', methods=['POST'])
def create():
    return create_battery_type()

@battery_type_blueprint.route('/battery_type/<int:id>', methods=['GET'])
def get(id):
    return get_battery_type(id)

@battery_type_blueprint.route('/battery_types', methods=['GET'])
def get_all():
    return get_all_battery_types()

@battery_type_blueprint.route('/battery_type/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_battery_type(id)
