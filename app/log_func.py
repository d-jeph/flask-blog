import os
import logging
from logging.handlers import RotatingFileHandler
from app import app

def setup_logger(log_file):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(log_file, maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')
