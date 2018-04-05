from flask_restplus import Namespace, Resource, fields
import app.core.system as system

api = Namespace('health_check', description='Domains and hosts health check')


@api.route('/domains/', methods=['GET'])
@api.route('/domains/<phase>', methods=['GET'])
class DoaminsHealthCheck(Resource):
    def get(self, phase=None):

        return system.check_domains(phase)


@api.route('/hosts/', methods=['GET'])
@api.route('/hosts/<phase>', methods=['GET'])
class HostsHealthCheck(Resource):
    def get(self, phase=None):
        return system.check_hosts(phase)