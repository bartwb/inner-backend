import logging
import os

# Directory for log files
LOG_DIR = "logs"

# Create the directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logger(name, log_file, level=logging.DEBUG):
    """
    Set up a specific logger with the given name and log file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler to log messages to a file
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, log_file))
    file_handler.setLevel(level)

    # Set format for logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger

# Initialize loggers for different models
battery_logger = setup_logger('battery_logger', 'log_battery.txt')
battery_type_logger = setup_logger('battery_type_logger', 'log_battery_type.txt')
battery_log_logger = setup_logger('battery_log_logger', 'log_battery_log_type.txt')
battery_finding_logger = setup_logger('battery_finding_logger', 'log_battery_finding.txt')
customer_logger = setup_logger('customer_logger', 'log_customer.txt')
customer_type_logger = setup_logger('customer_type_logger', 'log_customer_type.txt')
image_logger = setup_logger('image_logger', 'log_image.txt')

# General logging
app_logger = setup_logger('app_logger', 'app_log.txt')

