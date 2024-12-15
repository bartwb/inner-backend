from flask import Blueprint
from methods.battery_finding_manager import (
    create_battery_finding,
    get_battery_finding,
    get_all_battery_findings,
    update_battery_finding,
    delete_battery_finding
)

battery_finding_blueprint = Blueprint('battery_finding', __name__)

@battery_finding_blueprint.route('/battery_finding', methods=['POST'])
def create():
    return create_battery_finding()

@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['GET'])
def get(id):
    return get_battery_finding(id)

@battery_finding_blueprint.route('/battery_findings', methods=['GET'])
def get_all():
    return get_all_battery_findings()

@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['PUT'])
def update(id):
    return update_battery_finding(id)

@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_battery_finding(id)
