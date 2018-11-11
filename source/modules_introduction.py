from util.logger import get_logger
import os
from os import path
from glob import glob
import sys
logger = get_logger()

# ======================== os module   =========================== #
# -- is used to access underlying os functionality

logger.info(dir(os))
logger.info(dir(path))

logger.info(os.environ)
os.environ["VERSION"]="3.6"
logger.info(os.environ)
# logger.info(os.)

# os.walk is useful to traverse through given path recursively
logger.info(os.walk("."))
# logger.info(help(os.walk))
for root, dirs, files in os.walk("."):
    logger.info(root)
    logger.info(dirs)
    logger.info(files)

logger.info(glob("./Test*"))
#create directories,
#os.makedirs
#os.rename
#os.renames
#os.mkdir
#os.chmod
#os.chown
#os.remove
#os.removedirs
#os.rmdir

# os.path  # is useful to get all path related operations
logger.info(path.expanduser("~"))
logger.info(path.abspath("."))
logger.info(path.curdir)
logger.info(path.isdir("../config"))
logger.info(path.isfile("comments.py"))
logger.info(path.basename("~/Desktop/comments.py"))
logger.info(path.exists("~/Desktop/comments.py"))
# C:\\Desktop\newfile.py
# /desktop/newfile.py

logger.info(path.join(os.path.abspath("."),"newfile.py"))
logger.info(path.split("~/Desktop/comments.py"))  # ("~/Desktop/","comments.py")
logger.info(path.splitext("comments.py"))
logger.info(path.splitdrive(os.path.abspath(".")))
logger.info(path.sep)

# ===================== sys module -- To access Python language==================== #

logger.info(sys.platform)
logger.info(sys.version)
# argv is a list to save commandline arguments
# argparse
logger.info(sys.argv)

try:
    logger.info('Connecting to MySQl')
except Exception as e:
    logger.error("Failed to connect MySQL")
    sys.exit()

logger.info("This is after exit")

# =================== subprocess =================== #
import subprocess
logger.info(subprocess.check_output("dir", shell=True))

logger.info(subprocess.getstatusoutput("dir1"))
logger.info(subprocess.call("python hellow_world.py", shell=True))
cmd = subprocess.Popen("python sample_testfile.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# for line in cmd.stdout:
#     logger.info(line)

logger.info(cmd.stdout.readline())
cmd.stdin.write(b"TestUser\n")
cmd.stdin.flush()
rc = cmd.wait()

logger.info(cmd.stdout.readline())
logger.info(cmd.stdout.readline())

if rc!= 0:
    logger.error("Process Failed")

# To wait for process to complete
# rc = cmd.wait()
#
#
# if rc!=0:
#     logger.error("Process failed with an error ",cmd.stderr)

logger.info("New Line....")
#
# # =============== re -- regular Expression Module =================== #
# compile
# search
# match
# sub
from re import search, match, sub, compile, I

text = "Hello My Name is xyz and mail id xyz@gmail.com Hello"

# ^ -> Matches the beginning of a string
# $ -> Matched the end of a string
# * -> 0 to Many
# ? -> 0 or 1
# + -> More than 1
# \d -> To match digits
# \D -> To match Non-Digits
# \S -> To match Non Space
# \s  -> To match space
# [0-9, a-z, A-Z]

match_obj = match("(Hello)(.*)", text)

if match_obj:
    logger.info(match_obj.group(1))
    logger.info(match_obj.groups())

match_obj = search(r"(\S+)@Gmail.com$", text, I)
if match_obj:
    logger.info(match_obj.groups())


logger.info(sub("(Hello)","hello", text))
logger.info(text)

# match_obj = compile("(Hello).*")
# for line in open("Filename"):
#     match_obj.search(line)

compiled_pat = compile("^(Hello).*")
match_obj = compiled_pat.match(text, I)
#
#
# # ========================== datetime -- For date and time =========== #
from datetime import datetime, timedelta
# import time
# logger.info("Pause for 3 seconds")
# time.sleep(3)

logger.info(datetime.now())
current_dt = datetime.now()
logger.info(current_dt.year)
logger.info(current_dt.day)
logger.info(current_dt.month)
dt = datetime.strptime("21/11/09 16:10:02", "%d/%m/%y %H:%M:%S")
logger.info(dt)
logger.info(dt.strftime("%y-%m-%d"))

logger.info(datetime.now() - timedelta(days=10))
#
#
#
# # ============== threading =============== #
#
import threading


def calc_square(number):
    import time
    time.sleep(1)
    logger.info("Thead1 %s",number * number)


def calc_quad(number):
    logger.info("Thread2 %s",number * number * number * number)


number = 7
# thread1 = threading.Thread(target=calc_square, args=(number,))
# thread2 = threading.Thread(target=calc_quad, args=(number,))
# # Will execute both in parallel
# thread1.start()
# thread2.start()
# # Joins threads back to the parent process, which is this program
# thread1.join()
# thread2.join()
# #
# logger.info("Main Thread Exit")
#
# # ================= Networking ================= #

#
# if __name__ == "__main__":
#     # ================ multiprocessing =================== #
#     import multiprocessing
#     p1 = multiprocessing.Process(target=calc_square, args=(number,))
#     p2 = multiprocessing.Process(target=calc_quad, args=(number,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#
#

# # pandas
# # csv, openpyxl, lxml
# # RobotFramework
# # mysqlclient
# # Fabric
# # docker , jenkins
#
#


#
# def first(arg):
#     logger.info("Calling 1")
#     def decorator(f):
#         logger.info(f.__name__)
#         return f
#     return decorator
#
#
# def new_decorator(f):
#     logger.info("Calling 2")
#     logger.info(f.__name__)
#     def decorator2(arg):
#         return f(arg)
#     return decorator2
#
#
# @first("Hello this")
# @new_decorator
# def func(arg1):
#     logger.info("Calling")


# logger.info(func.__name__)