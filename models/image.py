from connection_manager import db

class Image(db.Model):  # Use db.Model for consistency
    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey("battery.id"), nullable=False)
    slide = db.Column(db.Integer, nullable=False)
    file_name = db.Column(db.String, nullable=False)
    blob_url = db.Column(db.String, nullable=False)

    # Establish relationship with Battery model
    battery = db.relationship("Battery", back_populates="images")  # Match the back_populates name in Battery

    def to_dict(self):
        return {
            "id": self.id,
            "battery_id": self.battery_id,
            "slide": self.slide,
            "file_name": self.file_name,
            "blob_url": self.blob_url,
            "battery": self.battery.to_dict() if self.battery else None,
        }
