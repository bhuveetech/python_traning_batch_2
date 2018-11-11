from util.logger import get_logger
from logging import DEBUG
import paramiko
import comments


logger = get_logger()

# dir help
#
# logger.info(dir(comments))

# help(comments.get_db_conn)
# help(comments)
# logger.info(dir(paramiko))
# help(paramiko.SSHClient)
# new_conn = paramiko.SSHClient()
# new_conn.connect()
#help(paramiko)



def sum1(a, b):
    """This is to sum of two numbers
    returns integer"""
    logger.info(locals())
    logger.info(vars())
    return a + b


# logger.info(sum1(1, 3))
# logger.info(sum1(2, 3))

# error = lambda a : a=20
sum_lam = lambda a, b: a+b
logger.info(sum_lam(1, 3))
# logger.info(sum_lam(2, 3))

# res = logger.info(20)
# logger.inf(res)
neg_lam = lambda a: logger.info(a)  # return None

logger.info(neg_lam(1))
#
# [a for a in [1,2,3,4] if a%2==0]
pos_lam = lambda : [a for a in [1,2,3,4] if a%2==0]
logger.info(pos_lam())
#
# a=20
# b=30
# (a<b)?

# Simulation of Ternary operator
# a = 20
# b =30
# res = a if a>b else b
# logger.info(res)
# if a<b:
#     res = a
# else:
#     res = b

if_else = lambda : "True" if 1<2 else "false"
# # logger.info(if_else())
#
# func_call_lam = lambda : sum_lam(1,3)
# lam_func_call = lambda : sum1(1,3)
#
# # logger.info(func_call_lam())
# # logger.info(lam_func_call())
#
# #help(sum1)
# # help(int)
#
# # logger.info(dir())
# # logger.info(dir(sum1))
# #
# # logger.info(dir(list))
# # logger.info(help(list.append))
#
# var = 70
#

# logger.info("Hello world", end="\t")
# logger.info("python")
#
# logger.info("Hello world","python", sep="-")
#
# logger.info(__name__)
#
# sum1(3,5)

num =1
# num()
logger.info(callable(sum1))

logger.info(dir(comments))

name = "xx"
logger.info(callable(name))
func= 'get_conn'
logger.info
logger.info(callable(comments.get_conn))

# for attr in dir(comments):
#     # logger.info(attr)
#     # logger.info(callable(eval(attr)))
    # if callable(attr):
    #     logger.info("%s is callable",attr)
#
# a = input("Enter any number for an argument a: ")
# b = input("Enter any number for an argument b: ")
# logger.info(sum1(int(a),int(b)))
#
#
#

# Global variable
a = 20


def func1(a, c=30):
    # local variable
    logger.info(locals())
    b = 20
    logger.info(locals())
    # logger.info(a)


def new_fun():
    a = 40
    c = 70
    logger.info(vars())
    logger.info(locals()) # {"a":40, "c":70}
    func1(a, c)  # func1(40 , 70)
    func1(**locals())    # a=40, c=70


# logger.info(b)
# func1(10)
# func1(10,60)
# logger.info(globals())
# new_fun()


# def func(**option):
#     if "run" in option:
#         # call this
#
#     if "updateserver" in option:
#         # call this


def func(a, c=40, *args, **kwargs):  # packing
    logger.info(vars())
    logger.info(locals())
    logger.info("a=%s",a)
    logger.info("c=%s",c)

dict1 = {"a":70,
         "c":30,
         "b":40}

func(dict1)   # func({"a":70,"c":30})
# func(**dict1)  # a=70, c=30 # func1(a=70, c=30)  **kwargs
# func(a=dict1["a"], c=dict1["b"])
func(**dict1)  # a=70, c=30, b=40     kwargs ={"b":40}


tuple1 = (30, 40, 60,70)
func(tuple1)  # func1((30, 40)) func1(tuple1)
# func(*tuple1)  # func1(30, 40)
# func(tuple1[0], tuple1[1])
#func1(tuple1[0], tuple1[21],..,...,..,..,..,..,..,..,..)
func(*tuple1)  # 30, 40, 60, 70  args = (60, 70)


# # help(input)
# # raw_input , input
# user_value = input("Enter any number:")
# logger.info(type(user_value))  # '12'
# input()

vars(str)

logger.info("1+1")
logger.info(eval("1+1"))

# user_value = eval(input("Enter any number:"))
exec("import time; logger.info(time.ctime())")


exec(compile("a=1;b=20;logger.info(a+b)","<string>","exec"))



# # ============ abs ============== #
logger.info(abs(1)) # 1
logger.info(abs(-1)) # 1


# =========== divmod ============= #
logger.info(divmod(4,2)) # (4//2, 4%2 ) -> (2, 0 )
logger.info(divmod(3,2)) # ( 3//2, 3%2) -> ( 1, 1)
logger.info(3//2)
logger.info(3%2)

# ============= max =============== #
#
# help(max)
logger.info(max(1,2,3)) # 3
logger.info(max("python"))  # y
logger.info(max("aython","baresh",key=lambda value:value[1]))  #
logger.info(max("",default="No value"))
logger.info(max("", default="empty value"))

# ============== min ============== #

logger.info(min(1,2,3)) # 1
logger.info(min("python"))  # h
logger.info(min("ay","bc"))  #  ay a bc b  -> a b -> ay
logger.info(min("ay","bc", key=lambda value:value[0]))
logger.info(min("ay","bc", key=lambda value:value[1]))  # ay -> y bc-> c # y c -> bc
logger.info(min("aython","baresh",key=lambda value:value[1]))  # y a -> baresh
logger.info(min("",default="No value"))

# ================ pow =============== #
logger.info(pow(2,3))
logger.info(2**3)

# ================ round ============= #
# 23.56 # single precision 23.6
# 23.54 # single precision 23.6
# 23.56 # 23.6 # 24

logger.info(round(23.56))   # 23.56 # 23.6 #  24
logger.info(round(23.56,1))  # 23.6
logger.info(round(23.56,2))  # 23.56

# ========== sum ================ #
logger.info(sum([1,2,3]))  # 1+2+3
logger.info(sum({20,30,40}))




# ================ all ================= #
a = 10
ret = all([a>=10, a<40]) # ([True, True]) -> True
logger.info(ret)
ret = a>=10 and a<40   # True -> True
logger.info(ret)
ret = 10 and 0    # 0
ret = 10 and 60 and 4*6  # 4*6 -> 24
logger.info(ret)
ret = all([10, 60, 4*6]) #  True
logger.info(ret)
logger.info(ret)
ret = all([0 , 2])
logger.info(ret)
ret = 0 and 2
logger.info(ret)
empty_re = all({})  # True
logger.info(empty_re)

# ================ any ======================== #
a = 10
ret = any([a>=10, a<40])
logger.info(ret)
ret = any([a<10, a>12])  # a<10 or a>12
logger.info(ret)
ret = any({0, 2, 3})  # True
logger.info(ret)
ret = any({0:"",
           2:"",
           3:""})
ret = any({0,2,3}) # True
logger.info(ret) # True
#
# # iterable -> string, list, tuple, dict, set, frozenset
# # "python" -> 'p' 'y' 't' 'h'
# # ["python", "java"] -> "python" "java"
# dict1 = {1: "python", 2: "java"} #-> {1, 2 } -> 1 2
# for key in dict1:
#     logger.info(key) # 1
#     logger.info(dict1[key])
#
# # ============= len ==================== #
logger.info(len("java"))  # 4
logger.info(len([12,'python',23.56, [23, 4, 5]])) # 4
#
#
# # ================= sorted =================== #
logger.info(sorted("python")) # ['h', 'n', 'o', 'p', 't', 'y']
logger.info(sorted([1,67,2,3])) # [1,2, 3, 67]
logger.info(sorted([1,67,2,3],reverse=True)) # [67,3,2,1]
#
def cmp_fun(value):
    return value[0]

logger.info(sorted(["ab","ba"])) # ["ab", "ba"] -> a b -> ab ba
logger.info(sorted(["ab","ba"],key=lambda value:value[0]))

# for value in ["ab","ba"]:
#     cmp_fun(value)

# lambda "ab": "ab"[0] -> a
# lambda "ba": "ba"[0] -> b
# ["ab", "ba"]

logger.info(sorted(["ab","ba"],key=lambda value: value[1]))
# lambda "ab": "ab"[1] -> b
# lambda "ba": "ba"[1] -> a
# ["ba", "ab"]
#
#
# # ================ hash ==================== #
# server hashli.64
logger.info(hash(1)) # hash value -> 1
logger.info(hash("python"))
logger.info(hash("python"))
logger.info(hash(12.34))
logger.info(hash(12.34))
#
# # ================ id =================== #
# logger.info(help(id))
a = 1
b =1
logger.info(id(a))
logger.info(id(b))
logger.info(id(1))
logger.info(id(1))
logger.info(id("python"))
logger.info(id("python"))
a = (1,2,34)
logger.info(id(a))
#
# # ============== chr ======================= #
# logger.info(chr(1))
# logger.info(chr(92))
# logger.info(chr(97))
# logger.info(chr(102))
# logger.info(chr(126))
# logger.info(chr(255))
# # logger.info(chr(257))
# # logger.info("{}".format(chr(257)))
# print(chr(257))

# ================= ord ====================== #
# logger.info(ord("a"))
# logger.info(chr(97))
# logger.info(ord("f"))
# logger.info("~")
# #ÿ
# #ā

# # ================= ascii =================== #
# logger.info(chr(255))
# logger.info(ascii('a'))
# logger.info(ascii(12))
# logger.info(ascii(chr(255)))
# logger.info(ascii(chr(127)))
# logger.info(ascii(chr(126)))
#
# # ================= bin =================== #
# logger.info(bin(10))
# logger.info(bin(20))
# logger.info(bin(8))

# map, reduce, filter  **
# range, zip , enumerate  ** range vs xrange
# yield vs return  # Generator

from functools import reduce
list1 = [1,2,3,4,5,6]
update_list = map(lambda value: value**2, list1)
logger.info(update_list)
for item in update_list:
    logger.info(item)

# map(fun, list_of)
logger.info(list(map(int, [1.2, 2.3, 3.4, 65])))
# int(1.2) , int(2.3), int(3.4), int(65)

# update_list = []
# for item in [1.2, 2.3, 3.4, 65]:
#     update_list.append(int(item))
# [int(item) for item in [1.2, 2.3, 3.4, 65]]
# filter(function, iterable)
logger.info(list(filter(None, [1,2,3,4,5,6])))

logger.info(list(filter(lambda value: value%2 == 0, [1,2,3,4,5,6])))

logger.info(reduce(lambda value1, value2: value1+value2,[1,2,3,4,5]))
import operator
logger.info(reduce(operator.add, [1,2,3,4,5]))
logger.info(reduce(lambda str1, str2: str1+str2, ['name1','name2', 'name3']))


# [1,2,3,4,5]
# (1+2)+3)+4)+5) ->  3, 3 , 6, 10,

# isinstance, issubclass, hasattr, delattr, setattr, classmethod, staticmethod

list_keys = [1,2,3]
list_values = ["name2","name2", "name3"]
zip_obj = zip(list_keys, list_values)
logger.info(list(zip(list_keys, list_values)))
logger.info(dict([(1,"name1"),(2,"name2")]))
logger.info(dict(zip_obj))

product_id_list = ["FUR-BO-10001798" , "FUR-CH-10000454" ,"OFF-LA-10000240" ,"FUR-TA-10000577"]
profit_list = [41.9136,219.582,6.8714]

logger.info(list(zip(product_id_list,profit_list)))
# product_id , profit = ("FUR-BO-10001798", 41.9136)
# logger.info(product_id, profit)

# [(product_id, profit), (proudct, profit)
for product_id, profit in zip(product_id_list, profit_list):
    logger.info("Profit value :%s for the product:%s",profit, product_id)


# import pandas as pd
# store_data = pd.read_excel("..\config\sample_superstore.xls")
# # logger.info(dir(store_data))
# logger.info(store_data.loc[store_data.Profit > 0, ["Discount","Profit"]])

# import random
# logger.info(random.choice([1,2,3,4]))
# select Discout, proft from table where proft >0
# select *from

#    Discount   Profit
# 0  0.3        1.2
# 1  4.5
# 2

list1 = [1,2,3,4,45]
# list1[start:end:step]

# range(2,10) -> [2,3,4,5,6,7,8,9]
# xrange(2,10) -> generator object  -> generate one value at a time upon calling
logger.info(list(range(2,10,1)))  #[2,3,4,5,6,7,8,9]

index = 0
for item in list1:
    logger.info("Index: %s, value:%s",index, item)
    index +=1

logger.info(list(enumerate(list1)))
for index,item in enumerate(list1):
    logger.info("Index: %s, value:%s",index, item)

# asyncio -- asynchronous program
# celery -- distribute task


def ret_func():
    a = 20
    b = 30
    logger.info("Function with return")
    return 1
    logger.info("Calling second time")
    return 2
    logger.info("Calling third time")
    return 3


def gen_func():
    a = 20
    b = 30
    logger.info("Function with Yield")
    # make a server request for file download
    yield 1
    a +=1
    b +=1
    logger.info("Calling second time")
    yield 2
    logger.info("Calling third time")
    yield 3

def get_all_data():
    for i in range(10):

        yield i
        # return i
def get_all_data_ret():
    for i in range(10):
        return i

res = ret_func()
res_gen = gen_func()
logger.info(res)
logger.info(res_gen)
# res_gen.send()

list1= [1,2,3,4,5]
# __iter__
# __next__
for item in list1:
    logger.info(list1)

logger.info(res_gen.__next__())
logger.info(res_gen.__next__())

gen_comprehension = (item for item in range(10))
logger.info(gen_comprehension)

logger.info(gen_comprehension.__next__())
logger.info(gen_comprehension.__next__())
logger.info(list(gen_comprehension))
logger.info(list(gen_comprehension))

res_loop = get_all_data()
logger.info(res_loop)
logger.info(list(res_loop))

logger.info(get_all_data_ret())
logger.info(get_all_data_ret())


# variables scopes

ran_a = 1


def outer_func():
    # global ran_a
    # ran_a = 20
    b = 30
    logger.info("Outer function ran_a:%s",ran_a)  # 20
    logger.info("Outer b:%s",b)

    def inner_fun():
        global ran_a
        nonlocal b
        ran_a = 20
        b = 40
        logger.info("inner function ran_a:%s",ran_a)  # 20
        logger.info("Outer b:%s",b)

    inner_fun()
    logger.info(b)

logger.info(ran_a)
outer_func()
logger.info(ran_a)  # 20


# I've 1 GB file . My Machine RAM is 500MB.
# Read data from a file and data should not be space.
# companyrecords.txt
def get_filter_data():
    fp = open("functions.py","r")
    list_of_lines = []
    for data in fp:
        if data.isspace():
            continue
        yield data
        # list_of_lines.append(data)

# generator or yield
# in whats ways a generator object created

for line in get_filter_data():
    logger.info(line)
    # other_func(line)


def handle_error(div_func):   # div_func = div_two_num
    logger.info(div_func)
    def modified_div_two_num(a,b):
        if b:
            return div_func(a,b)
        else:
            logger.warning("b value sent as 0 and there is no support")
            return 0
    return modified_div_two_num


@handle_error # div_two_num = handle_error(div_two_num) -> modified_div_two_num
def div_two_num(a, b):
    logger.info("a:%s, b:%s",a, b)
    return a/b

# 1234
# parameter a, b
# return a/b
# func_name div_two_num

# div_two_num = handle_error(div_two_num)
# new_var = div_two_num
# div_func = div_two_num
# div_two_num = get_filter_data

# div_fun = div_two_num
# div_two_num = modified_div_two_num

# logger.info(new_var(4,2))
logger.info(div_two_num(4,2))
logger.info(div_two_num(4,0))

handle_error(div_two_num)  # div_func = 1

# analysis, time duaration, update functions





