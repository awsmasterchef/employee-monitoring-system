import logging

# Configure logging to write to a file
logging.basicConfig(filename='logger.log', level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')


def log_info_msg(msg: str):
    logging.critical(msg)


# logging.debug('This is a debug message')
#
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
