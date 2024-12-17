from flask import Blueprint, request
from methods.battery_finding_manager import (
    create_battery_finding,
    get_battery_finding,
    get_all_battery_findings,
    get_battery_finding_by_image,
    get_battery_finding_by_battery,
    update_battery_finding,
    delete_battery_finding
)
from logger_config import battery_finding_logger  # Use existing logger

battery_finding_blueprint = Blueprint('battery_finding', __name__)

# Create Battery Finding
@battery_finding_blueprint.route('/battery_finding', methods=['POST'])
def create():
    battery_finding_logger.info("POST /battery_finding - Request to create a battery finding.")
    response = create_battery_finding()
    battery_finding_logger.info("POST /battery_finding - Response sent.")
    return response

# Get Battery Finding by ID
@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['GET'])
def get(id):
    battery_finding_logger.info(f"GET /battery_finding/{id} - Request to retrieve a battery finding.")
    response = get_battery_finding(id)
    battery_finding_logger.info(f"GET /battery_finding/{id} - Response sent.")
    return response

# Get All Battery Findings
@battery_finding_blueprint.route('/battery_findings', methods=['GET'])
def get_all():
    battery_finding_logger.info("GET /battery_findings - Request to retrieve all battery findings.")
    response = get_all_battery_findings()
    battery_finding_logger.info("GET /battery_findings - Response sent.")
    return response

# Get Battery Findings by Image ID
@battery_finding_blueprint.route('/battery_findings/image/<int:image_id>', methods=['GET'])
def get_by_image(image_id):
    battery_finding_logger.info(f"GET /battery_findings/image/{image_id} - Request to retrieve findings by image ID.")
    response = get_battery_finding_by_image(image_id)
    battery_finding_logger.info(f"GET /battery_findings/image/{image_id} - Response sent.")
    return response

# Get Battery Findings by Battery ID
@battery_finding_blueprint.route('/battery_findings/battery/<int:battery_id>', methods=['GET'])
def get_by_battery(battery_id):
    battery_finding_logger.info(f"GET /battery_findings/battery/{battery_id} - Request to retrieve findings by battery ID.")
    response = get_battery_finding_by_battery(battery_id)
    battery_finding_logger.info(f"GET /battery_findings/battery/{battery_id} - Response sent.")
    return response

# Update Battery Finding
@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['PUT'])
def update(id):
    battery_finding_logger.info(f"PUT /battery_finding/{id} - Request to update a battery finding.")
    battery_finding_logger.debug(f"Request data: {request.get_json()}")
    response = update_battery_finding(id)
    battery_finding_logger.info(f"PUT /battery_finding/{id} - Response sent.")
    return response

# Delete Battery Finding
@battery_finding_blueprint.route('/battery_finding/<int:id>', methods=['DELETE'])
def delete(id):
    battery_finding_logger.info(f"DELETE /battery_finding/{id} - Request to delete a battery finding.")
    response = delete_battery_finding(id)
    battery_finding_logger.info(f"DELETE /battery_finding/{id} - Response sent.")
    return response
