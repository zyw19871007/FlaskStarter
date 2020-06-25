# -*- coding: utf8 -*-
import argparse
import os
import random

import py_eureka_client.eureka_client as eureka_client

import src.common.log as log_util
from src import __version__

abspath = os.path.dirname(__file__)

log = log_util.get_logger()


def get_config(section='eureka', option='urls'):
    return log_util.get_config(section, option)


def get_server_url(eureka_server="http://172.16.50.2:12386/eureka/", app_name="ALGO-SERVER-MASTER"):
    application = {}
    untry_servers = eureka_server.split(",")
    tried_servers = []
    ok = False
    while len(untry_servers) > 0:
        url = untry_servers[0].strip()
        try:
            application = eureka_client.get_application(url, app_name=app_name)
        except Exception as e:
            log.info("Eureka server [%s] is down, use next url to try." % url)
            tried_servers.append(url)
            untry_servers = untry_servers[1:]
        else:
            ok = True
            break
    instances = application.instances
    eureka_client.stop()
    return instances


def get_ignite_ip_port():
    user_eureka = get_config(section='ignite', option='user_eureka')
    if user_eureka == '0':
        ignite_url = get_config(section='ignite', option='ip')
        result = {'ip': ignite_url, 'port': get_config(section='ignite', option='port')}
        log.info("get_ignite_ip_port:{}", result)
        return result
    try:
        instances = get_server_url(eureka_server=get_config())
        index = random.randint(0, len(instances))
        result = {'ip': instances[index].ipAddr, 'port': get_config(option='ignite_port')}
    except Exception as e:
        result = {'ip': '172.16.20.7', 'port': 20080}
        log.error('获取ip出现异常:{}', e)
    log.info("get_ignite_ip_port:{}", result)
    return result


def arg_conf():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version',
                        version='%(prog)s version : ' + __version__, help='show the version')

    parser.add_argument('--debug', '-d', action='store_true',
                        help='show the version',
                        default=False)
    parser.add_argument('--port', '-p', help='set server port', default=5000, type=int)
    parser.add_argument('--bind', '-b', help='set server bind ip', default='0.0.0.0', type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    get_ignite_ip_port()
