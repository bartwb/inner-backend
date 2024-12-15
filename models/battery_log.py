from datetime import datetime
from connection_manager import db


class BatteryLog(db.Model):  # Use db.Model for consistency
    __tablename__ = "battery_log"

    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey("battery.id"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationship to Battery
    battery = db.relationship("Battery", back_populates="logs")

    def to_dict(self):
        return {
            "id": self.id,
            "battery_id": self.battery_id,
            "timestamp": self.timestamp.isoformat(),
        }
