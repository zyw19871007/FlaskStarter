# -*- coding: utf8 -*-
import os
import random
from configparser import ConfigParser

import py_eureka_client.eureka_client as eureka_client

abspath = os.path.dirname(__file__)


def get_config(section='eureka', option='urls'):
    print('get_config')
    cfg = ConfigParser()
    cfg.read(abspath + '/../config.ini')
    return cfg.get(section, option)


def get_server_url(eureka_server="http://172.16.50.2:12386/eureka/", app_name="ALGO-SERVER-MASTER"):
    application = {}
    print('get_server_url')
    untry_servers = eureka_server.split(",")
    tried_servers = []
    ok = False
    while len(untry_servers) > 0:
        url = untry_servers[0].strip()
        try:
            application = eureka_client.get_application(url, app_name=app_name)
        except Exception as e:
            print("Eureka server [%s] is down, use next url to try." % url)
            tried_servers.append(url)
            untry_servers = untry_servers[1:]
        else:
            ok = True
            break
    instances = application.instances
    # print(instances)
    eureka_client.stop()
    return instances


def get_ignite_ip_port():
    try:
        instances = get_server_url(eureka_server=get_config())
        index = random.randint(0, len(instances))
        # print(index)
        # print(instances[index].ipAddr)
        # print(instances[index].port.port)
        result = {'ip': instances[index].ipAddr, 'port': get_config(option='ignite_port')}
    except Exception as e:
        result = {'ip': '172.16.20.7', 'port': 20080}
        print('获取ip出现异常', e)
    print(result)
    return result


if __name__ == '__main__':
    get_ignite_ip_port()
