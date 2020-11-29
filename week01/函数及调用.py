import logging
import datetime
import os
from pathlib import Path


def test_fuc():
    print('I love python')
    path = "C:\\Users\\杜家耀\\var"
    log_path = os.path.isdir(path)
    if log_path is not False:
        print("This folder is already exist")
    else:
        os.makedirs(path + './var' + './log' + './python-20201128')
        logging.basicConfig(filename="test.log",\
                            level = logging.DEBUG,\
                            datefmt="%Y-%m-%d %H-%M-%S",\
                            format = "%(asctime)s %(name)-8s %(levelname)-8s %(message)s",\
                            )
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')
test_fuc()
