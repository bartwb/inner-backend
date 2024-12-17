from flask import jsonify, request
from models.battery_log import BatteryLog
from connection_manager import db
from logger_config import battery_log_logger  # Import your logger

def create_battery_log():
    try:
        battery_log_logger.info("Received request to create a new battery log.")
        data = request.get_json()
        battery_log_logger.debug(f"Request data: {data}")

        battery_id = data.get('battery_id')

        if not battery_id:
            battery_log_logger.warning("Battery ID is missing in request.")
            return jsonify({'message': 'Battery ID is required'}), 400

        new_log = BatteryLog(battery_id=battery_id)
        db.session.add(new_log)
        db.session.commit()
        battery_log_logger.info(f"Battery log created successfully with ID: {new_log.id}")
        return jsonify(new_log.to_dict()), 201
    except Exception as e:
        battery_log_logger.error(f"Error creating battery log: {e}", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the battery log', 'error': str(e)}), 500

def get_battery_log(id):
    try:
        battery_log_logger.info(f"Received request to fetch battery log with ID: {id}")
        log = BatteryLog.query.filter_by(id=id).first()

        if not log:
            battery_log_logger.warning(f"Battery log with ID {id} not found.")
            return jsonify({'message': 'Battery log not found'}), 404

        battery_log_logger.info(f"Battery log with ID {id} retrieved successfully.")
        return jsonify(log.to_dict()), 200
    except Exception as e:
        battery_log_logger.error(f"Error fetching battery log with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the battery log', 'error': str(e)}), 500

def get_all_battery_logs():
    try:
        battery_log_logger.info("Received request to fetch all battery logs.")
        logs = BatteryLog.query.all()
        battery_log_logger.info(f"Fetched {len(logs)} battery logs.")
        return jsonify([log.to_dict() for log in logs]), 200
    except Exception as e:
        battery_log_logger.error("Error while fetching all battery logs.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching battery logs', 'error': str(e)}), 500

def delete_battery_log(id):
    try:
        battery_log_logger.info(f"Received request to delete battery log with ID: {id}")
        log = BatteryLog.query.filter_by(id=id).first()

        if not log:
            battery_log_logger.warning(f"Battery log with ID {id} not found.")
            return jsonify({'message': 'Battery log not found'}), 404

        db.session.delete(log)
        db.session.commit()
        battery_log_logger.info(f"Battery log with ID {id} deleted successfully.")
        return jsonify({'message': 'Battery log deleted successfully'}), 200
    except Exception as e:
        battery_log_logger.error(f"Error deleting battery log with ID {id}: {e}", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the battery log', 'error': str(e)}), 500
