from flask import jsonify, request
from models.battery_type import BatteryType
from connection_manager import db

def create_battery_type():
    try:
        data = request.get_json()
        name = data.get('name')
        serial_number = data.get('serial_number')

        if not name or not serial_number:
            return jsonify({'message': 'Name and serial number are required'}), 400

        new_type = BatteryType(name=name, serial_number=serial_number)
        db.session.add(new_type)
        db.session.commit()
        return jsonify(new_type.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the battery type', 'error': str(e)}), 500

def get_battery_type(id):
    try:
        battery_type = BatteryType.query.filter_by(id=id).first()
        if not battery_type:
            return jsonify({'message': 'Battery type not found'}), 404
        return jsonify(battery_type.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching the battery type', 'error': str(e)}), 500

def get_all_battery_types():
    try:
        types = BatteryType.query.all()
        return jsonify([battery_type.to_dict() for battery_type in types]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching battery types', 'error': str(e)}), 500

def delete_battery_type(id):
    try:
        battery_type = BatteryType.query.filter_by(id=id).first()
        if not battery_type:
            return jsonify({'message': 'Battery type not found'}), 404

        db.session.delete(battery_type)
        db.session.commit()
        return jsonify({'message': 'Battery type deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the battery type', 'error': str(e)}), 500
