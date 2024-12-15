from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from models.customer import Customer
from connection_manager import db

class CustomerType(db.Model):  # Use db.Model
    __tablename__ = "customer_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Back reference to customers
    customers = db.relationship("Customer", back_populates="customer_type")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
