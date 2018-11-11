# from util import logger
import logging as lg
from os import walk
import os
from comments import *
from comments import get_db_conn
from source import *
import util
import sys
# from . import comments
#import comments


logger = util.logger.get_logger(lg.DEBUG)
logger.info("Hello Module")

# main()
# get_db_conn()
# main()
# Searching flow
#  Current directory - package
#


logger.info(os.path.expanduser("~"))
logger.info(sys.path)
logger.info(os.path.abspath("./.."))
sys.path.append(os.path.abspath("./.."))
logger.info(sys.path)
# get_db_conn()
# PYATHONPATH = ""


def test_func():
    logger.info("Test Function")
    for files in walk("./"):
        logger.info(files)


logger.info("Test Module name is :%s", __name__)


if __name__ == "__main__":
    logger.info("Executing Test module directly")
    test_func()