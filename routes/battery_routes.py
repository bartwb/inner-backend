from flask import Blueprint
from methods.battery_manager import (
    create_battery,
    get_battery,
    get_all_batteries,
    update_battery,
    delete_battery
)

battery_blueprint = Blueprint('battery', __name__)

@battery_blueprint.route('/battery', methods=['POST'])
def create():
    return create_battery()

@battery_blueprint.route('/battery/<int:id>', methods=['GET'])
def get(id):
    return get_battery(id)

@battery_blueprint.route('/batteries', methods=['GET'])
def get_all():
    return get_all_batteries()

@battery_blueprint.route('/battery/<int:id>', methods=['PUT'])
def update(id):
    return update_battery(id)

@battery_blueprint.route('/battery/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_battery(id)
