from flask import Blueprint, request
from methods.image_manager import (
    create_image,
    get_image,
    get_all_images,
    delete_image
)
from logger_config import image_logger

image_blueprint = Blueprint('image', __name__)

@image_blueprint.route('/image', methods=['POST'])
def create():
    image_logger.info("POST /image - Request to create an image.")
    image_logger.debug(f"Request data: {request.get_json()}")
    response = create_image()
    image_logger.info("POST /image - Response sent.")
    return response

@image_blueprint.route('/image/<int:id>', methods=['GET'])
def get(id):
    image_logger.info(f"GET /image/{id} - Request to fetch image with ID {id}.")
    response = get_image(id)
    image_logger.info(f"GET /image/{id} - Response sent.")
    return response

@image_blueprint.route('/images', methods=['GET'])
def get_all():
    image_logger.info("GET /images - Request to fetch all images.")
    response = get_all_images()
    image_logger.info("GET /images - Response sent.")
    return response

@image_blueprint.route('/image/<int:id>', methods=['DELETE'])
def delete(id):
    image_logger.info(f"DELETE /image/{id} - Request to delete image with ID {id}.")
    response = delete_image(id)
    image_logger.info(f"DELETE /image/{id} - Response sent.")
    return response
