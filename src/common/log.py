import os
from configparser import ConfigParser

from logstash_async.formatter import LogstashFormatter
from logstash_async.handler import AsynchronousLogstashHandler
from loguru import logger

# import src.common.util as util
abspath = os.path.dirname(__file__)
hd_log = None


def get_config(section='eureka', option='urls'):
    try:
        # print('get_config')
        cfg = ConfigParser()
        cfg.read(abspath + '/../config.ini')
        return cfg.get(section, option)
    except:
        return None


def get_logger():
    global hd_log
    if hd_log is None:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('base_dir', BASE_DIR)
        log_file_path = os.path.join(BASE_DIR, 'Log/python-web.log')
        err_log_file_path = os.path.join(BASE_DIR, 'Log/python-web-err.log')
        logger.add(log_file_path, rotation="50 MB", encoding='utf-8')  # Automatically rotate too big file
        logger.add(err_log_file_path, rotation="50 MB", encoding='utf-8',
                   level='ERROR')  # Automatically rotate too big file
        # logstash
        logstash_ip = get_config('logstash', 'ip')
        if logstash_ip:
            logstash_port = get_config('logstash', 'port')
            logstash_handler = AsynchronousLogstashHandler(logstash_ip, int(logstash_port), database_path=None)
            logstash_formatter = LogstashFormatter(
                message_type='python-logstash',
                extra_prefix='',
                extra=dict(app_name='python-web'))
            logstash_handler.setFormatter(logstash_formatter)
            logger.add(sink=logstash_handler)
        hd_log = logger
    return hd_log


if __name__ == '__main__':
    print("log.info")
    get_logger().warning("测试")
    get_logger().error("测试")
