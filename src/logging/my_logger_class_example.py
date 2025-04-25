# my_logger_class_example.py
import logging

# Create and configure logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers if this gets imported multiple times
if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

