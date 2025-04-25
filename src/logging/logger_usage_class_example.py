# Example usage

from my_logger_class_example import logger

logger.debug("This is a debug message")     # Won't be shown (below INFO)
logger.info("This is an info message")      # Visible
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
