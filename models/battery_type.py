from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from connection_manager import db

# Battery Type Model
class BatteryType(db.Model):  # Use db.Model instead of DeclarativeBase
    __tablename__ = "battery_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    serial_number = db.Column(db.String, nullable=False)
    batteries = relationship("Battery", back_populates="battery_type")  # Ensure consistency with Battery

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'serial_number': self.serial_number
        }
