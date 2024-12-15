from flask import jsonify, request
from models.image import Image
from connection_manager import db

def create_image():
    try:
        data = request.get_json()
        battery_id = data.get('battery_id')
        slide = data.get('slide')
        file_name = data.get('file_name')
        blob_url = data.get('blob_url')

        if not battery_id or not slide or not file_name or not blob_url:
            return jsonify({'message': 'Battery ID, slide, file name, and blob URL are required'}), 400

        new_image = Image(
            battery_id=battery_id,
            slide=slide,
            file_name=file_name,
            blob_url=blob_url
        )
        db.session.add(new_image)
        db.session.commit()
        return jsonify(new_image.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while creating the image', 'error': str(e)}), 500

def get_image(id):
    try:
        image = Image.query.filter_by(id=id).first()
        if not image:
            return jsonify({'message': 'Image not found'}), 404
        return jsonify(image.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching the image', 'error': str(e)}), 500

def get_all_images():
    try:
        images = Image.query.all()
        return jsonify([image.to_dict() for image in images]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching images', 'error': str(e)}), 500

def delete_image(id):
    try:
        image = Image.query.filter_by(id=id).first()
        if not image:
            return jsonify({'message': 'Image not found'}), 404

        db.session.delete(image)
        db.session.commit()
        return jsonify({'message': 'Image deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the image', 'error': str(e)}), 500
