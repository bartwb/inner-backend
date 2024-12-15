from flask import jsonify, request
from models.battery_log import BatteryLog
from connection_manager import db

def create_battery_log():
    try:
        data = request.get_json()
        battery_id = data.get('battery_id')

        if not battery_id:
            return jsonify({'message': 'Battery ID is required'}), 400

        new_log = BatteryLog(battery_id=battery_id)
        db.session.add(new_log)
        db.session.commit()
        return jsonify(new_log.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the battery log', 'error': str(e)}), 500

def get_battery_log(id):
    try:
        log = BatteryLog.query.filter_by(id=id).first()
        if not log:
            return jsonify({'message': 'Battery log not found'}), 404
        return jsonify(log.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching the battery log', 'error': str(e)}), 500

def get_all_battery_logs():
    try:
        logs = BatteryLog.query.all()
        return jsonify([log.to_dict() for log in logs]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching battery logs', 'error': str(e)}), 500

def delete_battery_log(id):
    try:
        log = BatteryLog.query.filter_by(id=id).first()
        if not log:
            return jsonify({'message': 'Battery log not found'}), 404

        db.session.delete(log)
        db.session.commit()
        return jsonify({'message': 'Battery log deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the battery log', 'error': str(e)}), 500
