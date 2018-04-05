import os
from subprocess import Popen, PIPE
import logging as log


# 도메인 상태 체크 0보다 크면 정상
def dig_domain(domain):
    result = int(os.popen('dig +short {} | wc -l'.format(domain)).read())
    return False if result == 0 else True


# 호스트 핑 테스트
def ping_host(host):
    toping = Popen(['ping', '-c', '1', '-W', '500', host], stdout=PIPE)
    ouput = toping.communicate()[0]
    hostalive = toping.returncode

    if hostalive == 0:
        return True
    else:
        log.error('[PING] {} is unreachable. {}'.format(host, ouput))
        return False
