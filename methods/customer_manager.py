from flask import jsonify, request
from models.customer import Customer
from connection_manager import db
from models.customer_type import CustomerType
from logger_config import customer_logger  # Import the customer logger

def create_customer():
    try:
        customer_logger.info("Received request to create a new customer.")
        data = request.get_json()
        customer_logger.debug(f"Request data: {data}")

        name = data.get('name')
        street_name = data.get('street_name')
        house_number = data.get('house_number')
        city = data.get('city')
        country = data.get('country')
        phone_number = data.get('phone_number')
        email_address = data.get('email_address')
        customer_type_id = data.get('customer_type_id')

        if not name or not email_address or not customer_type_id:
            customer_logger.warning("Missing required fields: Name, email address, or customer type ID.")
            return jsonify({'message': 'Name, email address, and customer type ID are required'}), 400

        if Customer.query.filter_by(email_address=email_address).first():
            customer_logger.warning(f"Email address '{email_address}' already exists.")
            return jsonify({'message': 'Email address already exists'}), 400

        new_customer = Customer(
            name=name,
            street_name=street_name,
            house_number=house_number,
            city=city,
            country=country,
            phone_number=phone_number,
            email_address=email_address,
            customer_type_id=customer_type_id
        )
        db.session.add(new_customer)
        db.session.commit()
        customer_logger.info(f"Customer created successfully with ID {new_customer.id}.")
        return jsonify(new_customer.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        customer_logger.error("Error occurred while creating a new customer.", exc_info=True)
        return jsonify({'message': 'An error occurred while creating the customer', 'error': str(e)}), 500


def get_customer(id):
    try:
        customer_logger.info(f"Received request to fetch customer with ID {id}.")
        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            customer_logger.warning(f"Customer with ID {id} not found.")
            return jsonify({'message': 'Customer not found'}), 404
        customer_logger.info(f"Customer with ID {id} fetched successfully.")
        return jsonify(customer.to_dict()), 200
    except Exception as e:
        customer_logger.error(f"Error occurred while fetching customer with ID {id}.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the customer', 'error': str(e)}), 500


def get_all_customers():
    try:
        customer_logger.info("Received request to fetch all customers.")
        customers = Customer.query.all()
        customer_logger.info(f"Fetched {len(customers)} customers.")
        return jsonify([customer.to_dict() for customer in customers]), 200
    except Exception as e:
        customer_logger.error("Error occurred while fetching all customers.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching customers', 'error': str(e)}), 500


def update_customer(id):
    try:
        customer_logger.info(f"Received request to update customer with ID {id}.")
        data = request.get_json()
        customer_logger.debug(f"Request data: {data}")

        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            customer_logger.warning(f"Customer with ID {id} not found.")
            return jsonify({'message': 'Customer not found'}), 404

        # Handle updates field by field
        for key, value in data.items():
            if key == "customer_type":  # Handle relationship explicitly
                customer_logger.debug(f"Updating relationship 'customer_type' with value '{value}'.")
                if isinstance(value, dict) and "id" in value:
                    customer.customer_type = CustomerType.query.get(value["id"])
                else:
                    customer_logger.warning(f"Invalid format for 'customer_type': {value}")
            else:
                customer_logger.debug(f"Updating field '{key}' with value '{value}'.")
                setattr(customer, key, value)

        db.session.commit()
        customer_logger.info(f"Customer with ID {id} updated successfully.")
        return jsonify(customer.to_dict()), 200
    except Exception as e:
        customer_logger.error(f"Error occurred while updating customer with ID {id}.", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while updating the customer', 'error': str(e)}), 500


def delete_customer(id):
    try:
        customer_logger.info(f"Received request to delete customer with ID {id}.")
        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            customer_logger.warning(f"Customer with ID {id} not found.")
            return jsonify({'message': 'Customer not found'}), 404

        db.session.delete(customer)
        db.session.commit()
        customer_logger.info(f"Customer with ID {id} deleted successfully.")
        return jsonify({'message': 'Customer deleted successfully'}), 200
    except Exception as e:
        customer_logger.error(f"Error occurred while deleting customer with ID {id}.", exc_info=True)
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the customer', 'error': str(e)}), 500


def get_customer_by_email(email_address):
    try:
        customer_logger.info(f"Received request to fetch customer with email address '{email_address}'.")
        customer = Customer.query.filter_by(email_address=email_address).first()
        if not customer:
            customer_logger.warning(f"Customer with email address '{email_address}' not found.")
            return jsonify({'message': 'Customer not found'}), 404
        customer_logger.info(f"Customer with email address '{email_address}' fetched successfully.")
        return jsonify(customer.to_dict()), 200
    except Exception as e:
        customer_logger.error(f"Error occurred while fetching customer with email address '{email_address}'.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the customer by email', 'error': str(e)}), 500
