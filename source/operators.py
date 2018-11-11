""" For practising operators examples"""
import copy
from util import logger
import requests  # Web scraping
#import paramiko  # to connect remote machine over ssh/telenet/scp then run command and get o/p
import pandas
import xlrd
# =============== Arithmetic ================ #


logger = logger.get_logger()

a = 4
b = 2

logger.info(a + b)
logger.info(a - b)
logger.info(a / b)  # Python3 2.0 python2 2
logger.info(a // b)
logger.info(a % b)
logger.info(a ** b)

logger.info(3 / 2)    # 1.5
logger.info(3 // 2)   # 1
logger.info(3 // 2.0)  # 1.0

# ============== Assignment Operators ============= #
a = 4
a += 2  # 6  -> a = a + 2
logger.info(a)
a -= 2  # a -= 2  ->  a = a -2 -> 4
logger.info(a)
a *=2  # a = a * 2
#
# # ================= Relational Operators ================== #
# success_code = 200
# response_code = 500
logger.info(1 == 2)
logger.info("python" == "java")

res = requests.get("http://google.com")
logger.info(res.status_code)

logger.info(res.text)

logger.info(res.status_code == 200)
logger.info(res.status_code != 200)
logger.info(1 > 2)
logger.info(1 < 2)
logger.info(1 >= 2)
logger.info(1 <= 2)
logger.info("java" == "avaj")
#
# # ================== Logical/ Conditional Operators =========== #
# and or not
# && ||

# False -> zero number, and empty string, list, tuple, dictionary, set, frozenset, and None
# True

# not will change boolean value False to True and True to False
# =========== and ============= #
# if both True -> True
# else False
# 1 and 2 -> 2

# ============== or ============ #
# if any condition is True -> True
# else False
# 1 or 2 -> 1


status = []   # False
dict1 = {"1":22, "2":33}
# dict1 = {}
if not dict1:
    logger.error("Dictionary is Empty")
    logger.info("Program is exiting.....")
    exit()

logger.info(not status)  # True
logger.info(not "")     # True
logger.info(not 1)      # False
logger.info( not None)  # True
# logger.info( not 0)  # True
# logger.info( not 1)  # False
# status_code = 500
logger.info([] and 2)  # False > [] -> []
logger.info([] and 2)   # False -> []
logger.info(1 or [] )  # True -> 1

#
logger.info("status_code %s",res.status_code)

if res.status_code == 200 or res.status_code == 300:
    logger.info("Connection is succesful")
    logger.info(res.content)

elif res.status_code >=400 and res.status_code < 500:
    logger.error("Client side error")

elif res.status_code >=500 and res.status_code <600:
    logger.error(("Server side error"))



logger.info(1 and 2 )   # 2
logger.info("hello" and "World") # World
logger.info(1 or 2 ) # 1

# dict1 = {"1":"hello"}
dict1 = {}
content = dict1 and dict1["1"]
# content = dict1["1"]
logger.info(content)

# if dict1:
#     content = dict1["1"]
#
# if content:

# logger.info(0 and 1)   # 0
# logger.info( 1 and 20)   # 20
# logger.info({} and [])   # {}
# logger.info({} or 6)    # 6
#
# # logger.info({} and 6)   # {}
# # logger.info({} or 6)    # 6
# # logger.info(6 and {})   # {}
# # logger.info(6 or {})    # 6
# #
# # logger.info(6 and 7)   # 7
# # logger.info(6 or 7)     # 6
# #
# #
r = 13 and {} and 5  or [] and 6  # {} and 5 or [] and 6 -> {} or [] and 6 -> {} or [] -> []
logger.info(r)
r = 22 and [] or 32 and 0 or 67  # [] or 32 and 0 or 67 -> [] or 0 or 67  -> 0 or 67 -> 67
logger.info(r)



# #
# # a = 1
# # a = a+1
# # #
# # a and a+1 and logger.info(a)
# #
# # # ==================== Membership Operators ================ #
#
# logger.info(1 in 1)
logger.info("p" in "python")
logger.info("hello python".find("p"))
logger.info("hello python Langauge"["hello python".find("p"):])
logger.info("p" not in "python")
logger.info("python" in "p")  # False
logger.info("python" in "python")
logger.info("python"[::-1] in "python")

logger.info(120 in [240, 330, 120])
logger.info("py" in ["python", "pyt","java"])
logger.info("py" not in ["python", "pyt","java"])

logger.info("emp1" in {"emp1":1 , "emp2":2})
logger.info(1 in {"emp1":1 , "emp2":2})  # False Note: key existence
logger.info(1 in {"emp1":1 , "emp2":2}.values())  # 1 in  [1, 2]


# for i in iterable:    [1, 2,3 ] # i = list[0] # perform action # i = list[1] # perform

# #
# #
# # # ====================== #
a = 1
b = 1
logger.info(id(a))
logger.info(id(b))


# is None
dict1 = None
logger.info(id(dict1))
dict1 = {"1":"data"}
logger.info(id(dict1))
if dict1 is None:
    logger.error("Dictionary is not initialized")
# if dict1 is not None:
#     dict1.values()

if id(dict1) == id(None):
    logger.error("Dictionary is not initialized")


logger.info(a is b)
logger.info(id(a) == id(b))

if a is not b:
    logger.info("Not matching")

else:
    logger.info("Matching")

#
# logger.info(a is not b)  #= Address Identity Operator ============ #
# a = 1
#
# list1 = [1, 2, 3]
# list2 = copy.deepcopy(list1)
# logger.info(list1 is list2)  # False
# logger.info(list1 == list2)  # True
# #
# # # ========================== Bitwise Operators =================== #
a = 1
b = 2
# 000001  # 1
# 000010   # 2
logger.info(a & b)
# 000001
# 000010
# 000000  # &
# 000011  # 3
logger.info(a | b)

logger.info(a << 2 )
# 00000001  # 00000100 # 4
# 00000001 # 00000000
logger.info(a >> 2)
#
logger.info(a << 1)   # 0 0 0 1 << 2 -> 0 0 1 0 -> 3
logger.info(a >> 1)   # 0 0 0 1 >> 2 -> 0 0 0 0 -> 0
#
# ~, ^
#
# # =================  Operator Precedence ========================== #
logger.info(2*3+3) # 12  # 2*3 -> 6 +2
logger.info(2*3/2*2)  # 6/2 * 2  # 3.0 * 2


store_data =pandas.read_excel("sample_superstore.xls")
logger.info(store_data.keys)


