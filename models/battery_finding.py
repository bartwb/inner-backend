from sqlalchemy import JSON
from connection_manager import db

class BatteryFinding(db.Model):  # Use db.Model for consistency
    __tablename__ = "battery_finding"

    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey("battery.id"), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey("image.id"), nullable=False)
    annotation = db.Column(JSON, nullable=False)

    # Relationships
    battery = db.relationship("Battery", back_populates="findings")
    images = db.relationship("Image", back_populates="findings")

    def to_dict(self):
        return {
            "id": self.id,
            "battery_id": self.battery_id,
            "image_id": self.image_id,
            "annotation": self.annotation,
            "battery": self.battery.to_dict() if self.battery else None,
            "image": self.images.to_dict() if self.images else None,
        }
