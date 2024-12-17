import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from logger_config import app_logger

app_logger.info("Starting application setup in connection_manager.py")

# Naming conventions for database constraints
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# Attach metadata to declarative base
metadata = MetaData(naming_convention=naming_convention)
Base = declarative_base(metadata=metadata)

# Initialize Flask and SQLAlchemy
db = SQLAlchemy(model_class=Base, metadata=metadata)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('test.db')}"

app_logger.debug(f"Database URI set to: {app.config['SQLALCHEMY_DATABASE_URI']}")

# Enable CORS to allow cross-origin requests
app_logger.info("Enabling CORS for the application")
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize database migration
app_logger.info("Initializing Flask-Migrate for database migrations")
migrate = Migrate(app, db)

# Import models to ensure they're registered with SQLAlchemy
try:
    app_logger.info("Importing models...")
    from models.battery import Battery
    from models.battery_type import BatteryType
    from models.customer import Customer
    from models.customer_type import CustomerType
    from models.battery_log import BatteryLog
    from models.image import Image
    from models.battery_finding import BatteryFinding
    app_logger.info("Models imported successfully")
except Exception as e:
    app_logger.error(f"Error importing models: {e}", exc_info=True)
    raise e

# Initialize SQLAlchemy app context
try:
    app_logger.info("Initializing database with Flask app context")
    db.init_app(app)
    migrate.init_app(app, db)
    app_logger.info("Database initialized successfully")
except Exception as e:
    app_logger.error(f"Error initializing database: {e}", exc_info=True)
    raise e
