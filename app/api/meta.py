from flask_restplus import Namespace, Resource, fields
import app.core.system as system

api = Namespace('meta', description="meta data")


@api.route('/domains/', methods=['GET'])
@api.route('/domains/<phase>', methods=['GET'])
class Domains(Resource):
    def get(self, phase=None):
        return system.get_domains(phase)


@api.route('/hosts/', methods=['GET'])
@api.route('/hosts/<phase>', methods=['GET'])
class Hosts(Resource):
    def get(self, phase=None):
        return system.get_hosts(phase)