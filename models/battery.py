from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection_manager import db

# Battery Model
class Battery(db.Model):  # Inherit from db.Model
    __tablename__ = "battery"

    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String, unique=True, nullable=False)
    build_year = db.Column(db.String, unique=True, nullable=False)
    battery_type_id = db.Column(db.Integer, ForeignKey("battery_type.id"), nullable=True)
    customer_id = db.Column(db.Integer, ForeignKey("customer.id"), nullable=True)
    total_distance = db.Column(db.Integer, nullable=True)
    main_reason = db.Column(db.String, nullable=True)
    comment = db.Column(db.String, nullable=True)

       # Relationships
    battery_type = db.relationship("BatteryType", back_populates="batteries")
    customer = db.relationship("Customer")  # Define if Customer has back_populates

    # One-to-Many relationships
    logs = db.relationship("BatteryLog", back_populates="battery", cascade="all, delete-orphan")
    findings = db.relationship("BatteryFinding", back_populates="battery", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="battery", cascade="all, delete-orphan")


    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'build_year': self.build_year,
            'battery_type_id': self.battery_type_id,
            'customer_id': self.customer_id,
            'total_distance': self.total_distance,
            'main_reason': self.main_reason,
            'comment': self.comment,
            'battery_type': self.battery_type.to_dict() if self.battery_type else None,
            'customer': self.customer.to_dict() if self.customer else None
        }
