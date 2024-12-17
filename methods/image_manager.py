import logging
from flask import jsonify, request
from models.image import Image
from connection_manager import db
from logger_config import image_logger  # Import the image logger

def create_image():
    try:
        image_logger.info("Received request to create a new image.")
        data = request.get_json()
        image_logger.debug(f"Request data: {data}")

        battery_id = data.get('battery_id')
        slide = data.get('slide')
        file_name = data.get('file_name')
        blob_url = data.get('blob_url')

        if not battery_id or not slide or not file_name or not blob_url:
            image_logger.warning("Missing required fields: Battery ID, slide, file name, or blob URL.")
            return jsonify({'message': 'Battery ID, slide, file name, and blob URL are required'}), 400

        new_image = Image(
            battery_id=battery_id,
            slide=slide,
            file_name=file_name,
            blob_url=blob_url
        )
        db.session.add(new_image)
        db.session.commit()
        image_logger.info(f"Image created successfully with ID {new_image.id}.")
        return jsonify(new_image.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        image_logger.error("Error occurred while creating an image.", exc_info=True)
        return jsonify({'message': 'An error occurred while creating the image', 'error': str(e)}), 500

def get_image(id):
    try:
        image_logger.info(f"Received request to fetch image with ID {id}.")
        image = Image.query.filter_by(id=id).first()
        if not image:
            image_logger.warning(f"Image with ID {id} not found.")
            return jsonify({'message': 'Image not found'}), 404
        image_logger.info(f"Image with ID {id} fetched successfully.")
        return jsonify(image.to_dict()), 200
    except Exception as e:
        image_logger.error(f"Error occurred while fetching image with ID {id}.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching the image', 'error': str(e)}), 500

def get_all_images():
    try:
        image_logger.info("Received request to fetch all images.")
        images = Image.query.all()
        image_logger.info(f"Fetched {len(images)} images.")
        return jsonify([image.to_dict() for image in images]), 200
    except Exception as e:
        image_logger.error("Error occurred while fetching all images.", exc_info=True)
        return jsonify({'message': 'An error occurred while fetching images', 'error': str(e)}), 500

def delete_image(id):
    try:
        image_logger.info(f"Received request to delete image with ID {id}.")
        image = Image.query.filter_by(id=id).first()
        if not image:
            image_logger.warning(f"Image with ID {id} not found.")
            return jsonify({'message': 'Image not found'}), 404

        db.session.delete(image)
        db.session.commit()
        image_logger.info(f"Image with ID {id} deleted successfully.")
        return jsonify({'message': 'Image deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        image_logger.error(f"Error occurred while deleting image with ID {id}.", exc_info=True)
        return jsonify({'message': 'An error occurred while deleting the image', 'error': str(e)}), 500
