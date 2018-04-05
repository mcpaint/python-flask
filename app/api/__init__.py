from flask import Blueprint
from flask_restplus import Api

from .meta import api as meta
from .health_check import api as health_check

app = Blueprint('api', __name__, url_prefix='/api')
api = Api(app,
          doc="/",
          title='Gift Infra API',
          version='1.0',
          description='선물하기 인프라 API')


api.add_namespace(meta)
api.add_namespace(health_check)