from flask import Flask, current_app
from cache import cache
import app.core.utils as utils
from multiprocessing import Pool
import logging as log


@cache.cached(timeout=10 * 60)
def get_domains(p_phase):
    f = open("{}/domains".format(current_app.config['SAMPLE_DATA_PATH']), 'r')

    result = []
    for row in f.readlines():
        arry = row.split(',')

        phase = arry[0].strip()
        project = arry[1].strip()
        domains = arry[2].strip()

        for domain in domains.split():

            if p_phase is None:
                result.append({
                    'phase': phase,
                    'project': project,
                    'domain': domain
                })
            else:
                if phase == p_phase:
                    result.append({
                        'phase': phase,
                        'project': project,
                        'domain': domain
                    })
    f.close()
    return result


@cache.cached(timeout=10 * 60)
def get_hosts(p_phase):
    f = open("{}/hosts".format(current_app.config['SAMPLE_DATA_PATH']), 'r')

    result = []
    for row in f.readlines():
        arry = row.split(',')

        phase = arry[0].strip()
        project = arry[1].strip()
        host = arry[2].strip()

        if p_phase is None:
            result.append({
                'phase': phase,
                'project': project,
                'host': host
            })
        else:
            if phase == p_phase:
                result.append({
                    'phase': phase,
                    'project': project,
                    'host': host
                })
    f.close()
    return result


@cache.cached(timeout=5)
def check_domains(p_phase):
    pool = Pool(processes=int(current_app.config['CPU_COUNT']))

    domains = get_domains(p_phase)
    result = pool.map(set_domain_item, domains)
    return result


def set_domain_item(row={}):
    active = utils.dig_domain(row['domain'])
    row['active'] = active
    return row


@cache.cached(timeout=5)
def check_hosts(p_phase):
    pool = Pool(processes=int(current_app.config['CPU_COUNT']))

    hosts = get_hosts(p_phase)
    result = pool.map(set_host_item, hosts)

    return result


def set_host_item(row={}):
    active = utils.ping_host(row['host'])
    row['active'] = active
    return row
