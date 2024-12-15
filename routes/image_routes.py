from flask import Blueprint
from methods.image_manager import (
    create_image,
    get_image,
    get_all_images,
    delete_image
)

image_blueprint = Blueprint('image', __name__)

@image_blueprint.route('/image', methods=['POST'])
def create():
    return create_image()

@image_blueprint.route('/image/<int:id>', methods=['GET'])
def get(id):
    return get_image(id)

@image_blueprint.route('/images', methods=['GET'])
def get_all():
    return get_all_images()

@image_blueprint.route('/image/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_image(id)
