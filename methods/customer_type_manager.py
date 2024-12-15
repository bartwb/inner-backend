from flask import jsonify, request
from models.customer_type import CustomerType
from connection_manager import db

def create_customer_type():
    try:
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({'message': 'Name is required'}), 400

        new_type = CustomerType(name=name)
        db.session.add(new_type)
        db.session.commit()
        return jsonify(new_type.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the customer type', 'error': str(e)}), 500

def get_customer_type(id):
    try:
        customer_type = CustomerType.query.filter_by(id=id).first()
        if not customer_type:
            return jsonify({'message': 'Customer type not found'}), 404
        return jsonify(customer_type.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching the customer type', 'error': str(e)}), 500

def get_all_customer_types():
    try:
        types = CustomerType.query.all()
        return jsonify([customer_type.to_dict() for customer_type in types]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching customer types', 'error': str(e)}), 500

def delete_customer_type(id):
    try:
        customer_type = CustomerType.query.filter_by(id=id).first()
        if not customer_type:
            return jsonify({'message': 'Customer type not found'}), 404

        db.session.delete(customer_type)
        db.session.commit()
        return jsonify({'message': 'Customer type deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the customer type', 'error': str(e)}), 500
