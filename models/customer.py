from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection_manager import db

class Customer(db.Model):  # Use db.Model
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    street_name = db.Column(db.String, nullable=True)
    house_number = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    email_address = db.Column(db.String, nullable=False)
    customer_type_id = db.Column(db.Integer, ForeignKey("customer_type.id"), nullable=False)

    # Use string-based reference to avoid import issues
    customer_type = db.relationship("CustomerType", back_populates="customers")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'street_name': self.street_name,
            'house_number': self.house_number,
            'city': self.city,
            'country': self.country,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'customer_type_id': self.customer_type_id,
            'customer_type': self.customer_type.to_dict() if self.customer_type else None
        }
