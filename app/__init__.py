import logging
import os

from flask import Flask, render_template
from flask_compress import Compress
from cache import cache
from app.monitoring.monitoring_controller import monitoring
from app.main.main_conroller import api as main
from app.api import app as apis
from app.log.log import setup_logging
from flask_moment import Moment

moment = Moment()

# Logging
setup_logging

# Define the WSGI application object
app = Flask(__name__)
Compress(app)

config = {
    "dev": "config.DevConfig",
    "test": "config.TestConfig",
    "alpha": "config.AlphaConfig",
    "real": "config.RealConfig",
}

config_name = os.getenv('FLASK_CONFIGURATION', 'dev')
app.config.from_object(config[config_name])

logging.info("PHASE : {}".format(config_name))

# Load the configuration from the instance folder
if app.config.from_pyfile('config.py', silent=True):
    logging.info("Successfully read private configuration instance file.")

cache.init_app(app)
moment.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


# Bllueprints
logging.debug("Initializing Blueprints...")
app.register_blueprint(main)
app.register_blueprint(monitoring)
app.register_blueprint(apis)
