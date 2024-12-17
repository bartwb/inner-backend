import logging
from flask import jsonify
from connection_manager import app, db
from sqlalchemy.orm import configure_mappers
from routes.customer_routes import customer_blueprint
from routes.battery_routes import battery_blueprint
from routes.battery_finding_routes import battery_finding_blueprint
from routes.battery_log_routes import battery_log_blueprint
from routes.battery_type_routes import battery_type_blueprint
from routes.customer_type_routes import customer_type_blueprint
from routes.image_routes import image_blueprint

# Import the centralized app logger
from logger_config import app_logger

# Import all models explicitly to avoid circular imports
from models.battery import Battery
from models.battery_type import BatteryType
from models.customer import Customer
from models.customer_type import CustomerType
from models.battery_finding import BatteryFinding
from models.battery_log import BatteryLog
from models.image import Image

# Ensure all mappers are configured
try:
    configure_mappers()
    app_logger.info("Mappers configured successfully.")
except Exception as e:
    app_logger.error(f"Error configuring mappers: {e}", exc_info=True)

application = app

# Registering Blueprint routes
app_logger.info("Registering blueprints.")
try:
    app.register_blueprint(customer_blueprint, url_prefix='/api')
    app.register_blueprint(battery_blueprint, url_prefix='/api')
    app.register_blueprint(battery_finding_blueprint, url_prefix='/api')
    app.register_blueprint(battery_log_blueprint, url_prefix='/api')
    app.register_blueprint(battery_type_blueprint, url_prefix='/api')
    app.register_blueprint(customer_type_blueprint, url_prefix='/api')
    app.register_blueprint(image_blueprint, url_prefix='/api')
    app_logger.info("Blueprints registered successfully.")
except Exception as e:
    app_logger.error(f"Error registering blueprints: {e}", exc_info=True)

# Create tables after all models are registered
with app.app_context():
    try:
        db.create_all()
        app_logger.info("Database tables created successfully.")
    except Exception as e:
        app_logger.error(f"Error creating database tables: {e}", exc_info=True)

if __name__ == "__main__":
    app_logger.info("Starting Flask application.")
    try:
        app.run(host='0.0.0.0', port=5002)
        app_logger.info("Flask application running on port 5002.")
    except Exception as e:
        app_logger.error(f"Error starting Flask application: {e}", exc_info=True)
