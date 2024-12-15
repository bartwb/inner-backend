import logging
from flask import jsonify, request
from models.battery_finding import BatteryFinding
from connection_manager import db

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def create_battery_finding():
    try:
        logging.info("Received request to create a new battery finding.")
        data = request.get_json()
        logging.debug(f"Request data: {data}")

        battery_id = data.get('battery_id')
        annotation = data.get('annotation')

        if not battery_id or not annotation:
            logging.warning("Battery ID and/or annotation missing in request.")
            return jsonify({'message': 'Battery ID and annotation are required'}), 400

        new_finding = BatteryFinding(battery_id=battery_id, annotation=annotation)
        db.session.add(new_finding)
        db.session.commit()
        logging.info(f"Battery finding created successfully with ID: {new_finding.id}")
        return jsonify(new_finding.to_dict()), 201
    except Exception as e:
        logging.error(f"Error while creating battery finding: {e}", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the battery finding', 'error': str(e)}), 500

def get_battery_finding(id):
    try:
        logging.info(f"Received request to fetch battery finding with ID: {id}")
        finding = BatteryFinding.query.filter_by(id=id).first()

        if not finding:
            logging.warning(f"Battery finding with ID {id} not found.")
            return jsonify({'message': 'Battery finding not found'}), 404

        logging.info(f"Battery finding with ID {id} retrieved successfully.")
        return jsonify(finding.to_dict()), 200
    except Exception as e:
        logging.error(f"Error while fetching battery finding with ID {id}: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the battery finding', 'error': str(e)}), 500

def get_all_battery_findings():
    try:
        logging.info("Received request to fetch all battery findings.")
        findings = BatteryFinding.query.all()
        logging.info(f"Fetched {len(findings)} battery findings.")
        return jsonify([finding.to_dict() for finding in findings]), 200
    except Exception as e:
        logging.error("Error while fetching all battery findings.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching battery findings', 'error': str(e)}), 500

def update_battery_finding(id):
    try:
        logging.info(f"Received request to update battery finding with ID: {id}")
        data = request.get_json()
        logging.debug(f"Request data: {data}")

        finding = BatteryFinding.query.filter_by(id=id).first()

        if not finding:
            logging.warning(f"Battery finding with ID {id} not found.")
            return jsonify({'message': 'Battery finding not found'}), 404

        for key, value in data.items():
            setattr(finding, key, value)
            logging.debug(f"Updated {key} to {value} for battery finding ID {id}")

        db.session.commit()
        logging.info(f"Battery finding with ID {id} updated successfully.")
        return jsonify(finding.to_dict()), 200
    except Exception as e:
        logging.error(f"Error while updating battery finding with ID {id}: {e}", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while updating the battery finding', 'error': str(e)}), 500

def delete_battery_finding(id):
    try:
        logging.info(f"Received request to delete battery finding with ID: {id}")
        finding = BatteryFinding.query.filter_by(id=id).first()

        if not finding:
            logging.warning(f"Battery finding with ID {id} not found.")
            return jsonify({'message': 'Battery finding not found'}), 404

        db.session.delete(finding)
        db.session.commit()
        logging.info(f"Battery finding with ID {id} deleted successfully.")
        return jsonify({'message': 'Battery finding deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error while deleting battery finding with ID {id}: {e}", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the battery finding', 'error': str(e)}), 500
