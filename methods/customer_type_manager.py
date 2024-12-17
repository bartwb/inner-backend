from flask import jsonify, request
from models.customer_type import CustomerType
from connection_manager import db
from logger_config import customer_type_logger  # Import the customer type logger

def create_customer_type():
    try:
        customer_type_logger.info("Received request to create a new customer type.")
        data = request.get_json()
        customer_type_logger.debug(f"Request data: {data}")

        name = data.get('name')

        if not name:
            customer_type_logger.warning("Missing required field: 'name'.")
            return jsonify({'message': 'Name is required'}), 400

        new_type = CustomerType(name=name)
        db.session.add(new_type)
        db.session.commit()
        customer_type_logger.info(f"Customer type '{name}' created successfully with ID {new_type.id}.")
        return jsonify(new_type.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        customer_type_logger.error("Error occurred while creating a new customer type.", exc_info=True)
        return jsonify({'message': 'An error occurred while creating the customer type', 'error': str(e)}), 500


def get_customer_type(id):
    try:
        customer_type_logger.info(f"Received request to fetch customer type with ID {id}.")
        customer_type = CustomerType.query.filter_by(id=id).first()
        if not customer_type:
            customer_type_logger.warning(f"Customer type with ID {id} not found.")
            return jsonify({'message': 'Customer type not found'}), 404
        customer_type_logger.info(f"Customer type with ID {id} fetched successfully.")
        return jsonify(customer_type.to_dict()), 200
    except Exception as e:
        customer_type_logger.error(f"Error occurred while fetching customer type with ID {id}.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the customer type', 'error': str(e)}), 500


def get_all_customer_types():
    try:
        customer_type_logger.info("Received request to fetch all customer types.")
        types = CustomerType.query.all()
        customer_type_logger.info(f"Fetched {len(types)} customer types.")
        return jsonify([customer_type.to_dict() for customer_type in types]), 200
    except Exception as e:
        customer_type_logger.error("Error occurred while fetching all customer types.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching customer types', 'error': str(e)}), 500


def delete_customer_type(id):
    try:
        customer_type_logger.info(f"Received request to delete customer type with ID {id}.")
        customer_type = CustomerType.query.filter_by(id=id).first()
        if not customer_type:
            customer_type_logger.warning(f"Customer type with ID {id} not found.")
            return jsonify({'message': 'Customer type not found'}), 404

        db.session.delete(customer_type)
        db.session.commit()
        customer_type_logger.info(f"Customer type with ID {id} deleted successfully.")
        return jsonify({'message': 'Customer type deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        customer_type_logger.error(f"Error occurred while deleting customer type with ID {id}.", exc_info=True)
        return jsonify({'message': 'An error occurred while deleting the customer type', 'error': str(e)}), 500
