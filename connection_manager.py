from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
import os

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

#Attach metadata to declarative base
metadata = MetaData(naming_convention=naming_convention)
Base = declarative_base(metadata=metadata)

db = SQLAlchemy(model_class=Base, metadata=(MetaData(naming_convention=naming_convention)))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('test.db')}"

#Enable CORS to allow browsers to make cross-origin requests
CORS(app, resources={r"/*": {"origins": "*"}})

migrate = Migrate(app,db)

# Import all models to register them with SQLAlchemy
from models.battery import Battery
from models.battery_type import BatteryType
from models.customer import Customer
from models.customer_type import CustomerType
from models.battery_log import BatteryLog
from models.image import Image
from models.battery_finding import BatteryFinding

db.init_app(app)
migrate.init_app(app, db)