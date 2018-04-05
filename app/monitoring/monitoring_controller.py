from flask import Blueprint, render_template
import app.core.system as system

# Define the blueprint: 'auth', set its url prefix: app.url/auth
monitoring = Blueprint('monitoring', __name__, url_prefix='/monitoring')


@monitoring.route('/domains', defaults={'phase': 'real'}, methods=['GET'])
@monitoring.route('/domains/<phase>', methods=['GET'])
def domains(phase):
    service = "monitorDomains"
    title = '선물하기 도메인 체크'
    return render_template(
        'monitoring/domains_monitoring.html',
        service=service,
        phase=phase,
        title=title,
        list=system.check_domains(phase),
    )


@monitoring.route('/hosts', defaults={'phase': 'real'}, methods=['GET'])
@monitoring.route('/hosts/<phase>', methods=['GET'])
def hosts(phase):
    service = "monitorHosts"
    title = '선물하기 서버 체크'
    return render_template(
        'monitoring/hosts_monitoring.html',
        service=service,
        phase=phase,
        title=title,
        list=system.check_hosts(phase),
    )
