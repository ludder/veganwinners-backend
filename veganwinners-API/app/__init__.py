import logging
from flask import Flask
from app.database import db_session, init_db
from app.recipes import recipes_blueprint
from app import config
from flask_cors import CORS
from app.custom_logger import setup_logger
from app.helpers import return_result

logger = logging.getLogger()
logger.handlers = []
setup_logger(logger)

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(recipes_blueprint, url_prefix='/api/recipes')

@app.errorhandler(500)
def server_error(e):
    return return_result(code=500, status="error", message=str(e))
