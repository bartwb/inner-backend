from flask import jsonify, request
from models.battery_type import BatteryType
from connection_manager import db
from logger_config import battery_type_logger  # Import the battery type logger

def create_battery_type():
    try:
        battery_type_logger.info("Received request to create a new battery type")
        data = request.get_json()
        battery_type_logger.debug(f"Request data: {data}")

        name = data.get('name')
        serial_number = data.get('serial_number')

        if not name or not serial_number:
            battery_type_logger.warning("Missing required fields: name or serial_number")
            return jsonify({'message': 'Name and serial number are required'}), 400

        new_type = BatteryType(name=name, serial_number=serial_number)
        battery_type_logger.debug(f"New BatteryType object: {new_type}")

        db.session.add(new_type)
        db.session.commit()
        battery_type_logger.info(f"Battery type created successfully with ID: {new_type.id}")
        return jsonify(new_type.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        battery_type_logger.error(f"Error while creating battery type: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while creating the battery type', 'error': str(e)}), 500


def get_battery_type(id):
    try:
        battery_type_logger.info(f"Received request to fetch battery type with ID: {id}")
        battery_type = BatteryType.query.filter_by(id=id).first()

        if not battery_type:
            battery_type_logger.warning(f"Battery type with ID {id} not found")
            return jsonify({'message': 'Battery type not found'}), 404

        battery_type_logger.info(f"Battery type with ID {id} retrieved successfully")
        return jsonify(battery_type.to_dict()), 200
    except Exception as e:
        battery_type_logger.error(f"Error while fetching battery type with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the battery type', 'error': str(e)}), 500


def get_all_battery_types():
    try:
        battery_type_logger.info("Received request to fetch all battery types")
        types = BatteryType.query.all()
        battery_type_logger.info(f"Fetched {len(types)} battery types")
        return jsonify([battery_type.to_dict() for battery_type in types]), 200
    except Exception as e:
        battery_type_logger.error("Error while fetching all battery types", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching battery types', 'error': str(e)}), 500


def delete_battery_type(id):
    try:
        battery_type_logger.info(f"Received request to delete battery type with ID: {id}")
        battery_type = BatteryType.query.filter_by(id=id).first()

        if not battery_type:
            battery_type_logger.warning(f"Battery type with ID {id} not found")
            return jsonify({'message': 'Battery type not found'}), 404

        battery_type_logger.info(f"Deleting battery type with ID {id}")
        db.session.delete(battery_type)
        db.session.commit()
        battery_type_logger.info(f"Battery type with ID {id} deleted successfully")
        return jsonify({'message': 'Battery type deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        battery_type_logger.error(f"Error while deleting battery type with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while deleting the battery type', 'error': str(e)}), 500
