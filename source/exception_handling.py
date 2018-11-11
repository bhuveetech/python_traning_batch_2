"""Exception handling
#
try:
    # block of statements

except Error as e:
    pass

else:
    pass

finally:
    pass
"""
import requests
from requests.exceptions import  ConnectionError
from util.logger import get_logger
from logging import DEBUG
logger = get_logger(DEBUG)


try:
    list1 = [1,2,3,4]
    logger.info(list1[0])
    dict = {}
    dict["name"]
    tuple1 = (1,)
    tuple1[2] = 30


except IndexError as e:
    logger.error("Index out of range:%s",e.args)

except KeyError as e:
    logger.error("%s Key is not found", e.args[0])
    dict['name'] = None

except TypeError as e:
    logger.error("Error in Tuple assignment")

except Exception as e:
    logger.error('Error appeared duing execution:%s',e)

else:
    logger.info("No Exception occurred")

logger.info("It runs with or without exception")
# try:
#     dict = {}
#     dict["name"]
#
# except KeyError as e:
#     logger.error("'%s' Key is not found",e.args[0])

try:
    requests.get("https://naresh.com")

except ConnectionError as e:
    logger.info("Failed to connect the given url, Check internet connectivity or URL")


try:
    fp = open("NewFile1.txt")
    fp.write("Hello this writing to file")

except IOError as e:
    logger.info("Problem with file writing:%s",e)

finally:
    if fp:
        fp.close()

    logger.info("Executing ......")


port_range = 8080


if port_range != 8080:
    raise RuntimeError("The given port is not 8080 port","2")


# request.connect(url, port, )
# urllib2



# User Defined Exception


class MyException(Exception):

    def __init__(self, message):
        self.msg = message



# Exception Block
try:
    raise MyException("Hello")

except MyException as e:
    logger.error(e.msg)


# A python program to create user-defined exception
