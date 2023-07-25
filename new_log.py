import logging
import time
from logstash_async.handler import AsynchronousLogstashHandler

host = 'localhost'
port = 9300

test_logger = logging.getLogger('python-logging-test')

test_logger.setLevel(logging.DEBUG)

async_handler = AsynchronousLogstashHandler(host, port, database_path=None)

test_logger.addHandler(async_handler)

while True:
    test_logger.info("hello this is first logging")
    time.sleep(0.5)