from flask import jsonify, request
from models.battery import Battery
from models.customer import Customer
from models.battery_type import BatteryType
from connection_manager import db
from logger_config import battery_logger  # Import the battery logger


def create_battery():
    try:
        battery_logger.info("Received request to create battery")
        data = request.get_json()
        battery_logger.debug(f"Request data: {data}")

        serial_number = data.get('serial_number')
        build_year = data.get('build_year')
        battery_type_id = data.get('battery_type_id')
        customer_id = data.get('customer_id')
        total_distance = data.get('total_distance')
        main_reason = data.get('main_reason')
        comment = data.get('comment')

        if not serial_number or not build_year:
            battery_logger.warning("Missing required fields: serial_number or build_year")
            return jsonify({'message': 'Serial number and build year are required'}), 400

        if Battery.query.filter_by(serial_number=serial_number).first():
            battery_logger.warning(f"Battery with serial_number {serial_number} already exists")
            return jsonify({'message': 'Serial number already exists'}), 400

        if Battery.query.filter_by(build_year=build_year).first():
            battery_logger.warning(f"Battery with build_year {build_year} already exists")
            return jsonify({'message': 'Build year already exists'}), 400

        battery_logger.info("Creating new battery object")
        new_battery = Battery(
            serial_number=serial_number,
            build_year=build_year,
            battery_type_id=battery_type_id,
            customer_id=customer_id,
            total_distance=total_distance,
            main_reason=main_reason,
            comment=comment
        )
        battery_logger.debug(f"New battery object: {new_battery}")

        db.session.add(new_battery)
        db.session.commit()
        battery_logger.info("Battery created successfully")
        return jsonify(new_battery.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        battery_logger.error(f"Error creating battery: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while creating the battery', 'error': str(e)}), 500


def get_battery(id):
    try:
        battery_logger.info(f"Received request to fetch battery with ID {id}")
        battery = Battery.query.filter_by(id=id).first()
        if not battery:
            battery_logger.warning(f"Battery with ID {id} not found")
            return jsonify({'message': 'Battery not found'}), 404
        battery_logger.info(f"Fetched battery: {battery}")
        return jsonify(battery.to_dict()), 200
    except Exception as e:
        battery_logger.error(f"Error fetching battery with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the battery', 'error': str(e)}), 500


def get_all_batteries():
    try:
        battery_logger.info("Received request to fetch all batteries")
        batteries = Battery.query.all()
        battery_logger.info(f"Fetched {len(batteries)} batteries")
        return jsonify([battery.to_dict() for battery in batteries]), 200
    except Exception as e:
        battery_logger.error("Error fetching all batteries", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching batteries', 'error': str(e)}), 500


def update_battery(id):
    try:
        battery_logger.info(f"Received request to update battery with ID {id}")
        data = request.get_json()
        battery_logger.debug(f"Request data: {data}")

        battery = Battery.query.filter_by(id=id).first()
        if not battery:
            battery_logger.warning(f"Battery with ID {id} not found")
            return jsonify({'message': 'Battery not found'}), 404

        battery_logger.info("Updating battery fields")
        for key, value in data.items():
            # Handle relationship fields explicitly
            if key == "battery_type" and isinstance(value, dict):
                battery_logger.debug(f"Updating 'battery_type' relationship with value: {value}")
                battery.battery_type = BatteryType.query.get(value["id"])
            elif key == "customer" and isinstance(value, dict):
                battery_logger.debug(f"Updating 'customer' relationship with value: {value}")
                battery.customer = Customer.query.get(value["id"])
            elif hasattr(battery, key):
                battery_logger.debug(f"Updating field {key} to {value}")
                setattr(battery, key, value)

        db.session.commit()
        battery_logger.info(f"Battery with ID {id} updated successfully")
        return jsonify(battery.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        battery_logger.error(f"Error updating battery with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while updating the battery', 'error': str(e)}), 500


def delete_battery(id):
    try:
        battery_logger.info(f"Received request to delete battery with ID {id}")
        battery = Battery.query.filter_by(id=id).first()
        if not battery:
            battery_logger.warning(f"Battery with ID {id} not found")
            return jsonify({'message': 'Battery not found'}), 404

        battery_logger.info(f"Deleting battery with ID {id}")
        db.session.delete(battery)
        db.session.commit()
        battery_logger.info(f"Battery with ID {id} deleted successfully")
        return jsonify({'message': 'Battery deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        battery_logger.error(f"Error deleting battery with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while deleting the battery', 'error': str(e)}), 500
