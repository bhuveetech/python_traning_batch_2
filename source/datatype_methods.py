"""To Practise data types methods"""
# dir help

import logging
import comments
import subprocess
import pprint

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s- %(levelname)s - %(filename)s-%(lineno)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

# logger.debug(dir("python"))
# logger.debug(dir(str))

# logger.debug(help(str.join))


# logger.debug("welcome to python".capitalize())
# logger.debug("python".istitle())
# logger.debug("python".islower())
# logger.debug("The converted message %s","welcome to python".title())
#
# logger.debug("python".isalpha())
#
# user_input = "123s"
# logger.debug(user_input.isdecimal())
#
# logger.debug("123".isdecimal())
#
# logger.debug(user_input.isalnum())
#
# logger.debug("python".isspace())
# logger.debug("\n".isspace())
# logger.debug("\t".isspace())
# logger.debug(" ".isspace())
#
# up_var = "python".upper()
# low_var = up_var.lower()
# logger.debug(up_var.isupper())
# logger.debug(low_var.islower())
#
#
# logger.debug("python".swapcase())
# logger.debug("Python".swapcase())
#
# logger.debug("python".endswith("hon"))
# logger.debug("python".startswith("pyt"))


## split, splitlines, rsplit, strip, lstrip, rstrip, join, find,rfind, index,rindex, replace
logger.info(dir(str))
# logger.info(dir(comments))
# # logger.info(help(comments))
# logger.info(help(comments.get_db_conn))
#logger.info(help(str.split))

# message = "welcome to python"
# logger.info(message.split())
# logger.info(message.split(maxsplit=1))
# ip_address = "127.0.0.1"
# #             012345678
# list_of_octal = ip_address.split(".")
# logger.info(list_of_octal)
# file_name = "test.py"
# #            0123456
# logger.info(file_name.split("."))
# logger.info(file_name.split(".")[0])
#
# logger.info(message.rsplit(maxsplit=1))
#
# logger.info(ip_address.split(sep='.',maxsplit=1))  # 127 0.0.1
# logger.info(ip_address.rsplit(sep='.',maxsplit=1))  # 127.0.0  1
#
# logger.info(file_name.strip("py."))
#
# message1 = "0010hello world 0000"
# logger.info(message1.strip('0'))
# logger.info(message1.lstrip('0'))
# logger.info(message1.rstrip('0'))
#
# server_message = "\n hello this is messgae in server\n"
# logger.info(server_message.strip())
#
# logger.info(file_name.find(".py"))  # 4
# logger.info(file_name.find(".txt"))  # -1
#
# logger.info(file_name.index(".py"))  # 4
# # logger.info(file_name.index(".txt"))
# if file_name.find(".py")!=-1:
#     print("file is python file")
# else:
#     print("Not python file")
#
#
# logger.info(ip_address.find("."))
# logger.info(ip_address.rfind("."))
# logger.info(ip_address.index("."))
# logger.info(ip_address.rindex("."))
#
#
# different_message = ["Welcome to python", "Welcome to Java", "Welcome to scala"]
# # slicing with rfind
# for message in different_message:
#     logger.info(message[message.rfind(" ")+1:])
#
# logger.info(different_message[0].rfind(" "))
# logger.info(different_message[0].find(" "))
#
#
# message5 = "Hello this is Network message \n from Ip address 127.0.0.1"
# logger.info(message5.splitlines())

# output = subprocess.getoutput("dir")
# logger.info(output)
# logger.info(output.splitlines())
# #
# logger.info("{form} Finding python files {form}".format(form="="*12))
# for line in output.splitlines():
#     # print(line)
#     if line.find(".py")!=-1:
#         logger.info(line)


# Fina a hell_world.py file then execute it using subprocess

# list_of_ips = ["127.0.0.1","10.0.0.2","10.3.4.5"]

# help(str.join)

# logger.info("\n".join(list_of_ips))

# "127.0.0.1\n10.0.0.2\n10.3.4.5"

# ip_addr = "127.0.0.1"
# list_of_octal = ip_addr.split(".")
# logger.info(list_of_octal)
# list_of_octal[0] = "10"
# logger.info(list_of_octal)
# logger.info(".".join(list_of_octal))


# Find your machine ip address using subprocess module. ipconfig .. ifconfig
# subprocess

ip_addr = "127.0.0.1"
# list_of_octal = ip_addr.split(".")
# logger.info(list_of_octal)
new_ip_addr =ip_addr.replace("127","10")
# logger.info(list_of_octal)
# logger.info(".".join(list_of_octal))
# logger.info("NewIP address: {new_ip} OldIp address:{old_ip}".format(new_ip=new_ip_addr,
#                                                                     old_ip=ip_addr))
#
# logger.info(ip_addr.replace(".",":",3))
# logger.info(ip_addr.replace(".",":",1))
#
# logger.info(dir(str))


# logger.info(ip_addr.replace(".",":",ip_addr.count(".")))
# # count, center, ljust, rjust, zfill
# logger.info(ip_addr.ljust(20,"x"))
# logger.info(ip_addr.rjust(20,'x'))
# logger.info(ip_addr.center(20,'x'))
# logger.info(ip_addr.zfill(20))
#
# logger.info(ip_addr.center(20))


# ================== Tuple ======================= #
#
# dir, help
# logger.info(dir(tuple))
# logger.info(help(tuple.count))

list_of_names = ("xyz", "yz", "zz","xyz", "mm", 12, 234)
# logger.info(list_of_names.count("xyz"))
#
# logger.info(list_of_names.count("zz"))
#
# logger.info(list_of_names.count(2000))

# logger.info(help(tuple.index))

# logger.info(list_of_names.index("mm")) # 4
#
# # logger.info(list_of_names.index('2345'))
# logger.info(list_of_names.index("mm",0,5))


# ======================== List =========================== #
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# modifiying existing list (append, insert, extend) , Removing ( pop, remove, clear)
# index
# reverse , sort
# copy
# count

logger.info(dir(list))
#logger.info(help(list.append))

list_of_data = []
logger.info((list_of_data))
list_of_data.append(12)
logger.info((list_of_data))
list_of_data.append(list_of_names)
logger.info(list_of_data)
list_of_data.append("Hello world")
logger.info(list_of_data)

logger.info(list_of_data[1])  # ("xyz", "yz", "zz","xyz", "mm", 12, 234)

# i need to retrieve last word from the string in given list
# slicing, rfind, negative indexing
list_of_data[2]
list_of_data[-1]

logger.info(list_of_data[-1]) # "Hello world"[list_of_data[-1].rfind(" "):]
logger.info(list_of_data[-1].split())
logger.info(list_of_data[-1].split()[1])

dict1 = {"lang1":"python",
         "lang2":"java"}


list_of_data.append(dict1)
logger.info(list_of_data)


# To acces "lang1" value from list of data
logger.info(list_of_data[-1]["lang1"])
logger.info(list_of_data[-1]["lang1"][-1])

# pprint.pprint(list_of_data)

#list_of_data.insert()
list_of_data.insert(0, 2000)
# pprint.pprint(list_of_data)

# pprint.pprint(list_of_data[2])
list_of_data.insert(2, "New Data")
# pprint.pprint(list_of_data)
logger.info(list_of_data)

new_list_data = ["network1","network2","network3"]

list_of_data.append(new_list_data)
logger.info(list_of_data)

list_of_data.pop(-1)
new_modify = list_of_data + new_list_data  # O(n) + O(k)  # O(K)
logger.info(new_modify)
logger.info(list_of_data)


list_of_data.extend(new_list_data)  # O(K)
logger.info(list_of_data)


list_of_data.clear()
logger.info(list_of_data)

list_of_data.extend(dict1)
logger.info(list_of_data)

list_of_data.remove('lang1')
list_of_data.remove('lang2')
logger.info(list_of_data)

list_of_data.append(dict1)
logger.info(list_of_data)

list_of_data.pop()
logger.info(list_of_data)
list_of_data.extend(dict1)
logger.info(list_of_data)
list_of_data.pop(0)  # pop() pop(-1 or len(list)-1)
logger.info(list_of_data)

list_of_data.clear()

list_of_data.extend(dict1)
logger.info(list_of_data)
logger.info(list_of_data.index("lang1"))
logger.info(list_of_data.index("lang2"))

logger.info(list_of_data.count('lang1'))
logger.info(list_of_data.count(2000))


new_list = [20, 2, 4, 70, 9, 12, 5]
new_list.sort()  # without reverse , sorted in ascending order else descending order
logger.info(new_list)

new_data = ["xx", "yy", "ab", "dn"]  # x y a d  # a d x y # y x d a # yy xx dn ab
new_data.sort(reverse=True)

logger.info(new_data)

new_data.sort()   # x y a d  # a d x y # ab dn xx yy
logger.info(new_data)
new_data.sort(key=lambda item: item[1])  # x y b n # b n x y # ab dn xx yy
logger.info(new_data)

list_of_emails = ["xa@gmail.com", "ac@yahoo.com","zb@gmail.com"]
list_of_emails.sort()   # ac@yahoo.co, xa@gmail.com zb@gmail.com
list_of_emails.sort(key=lambda  item:item[0])
logger.info(list_of_emails)

list_of_emails.sort(key=lambda item: item[1])  #  [ 'a', 'c', 'b']  #
logger.info(list_of_emails)      # xa@gmail.com zb@gmail.com ac@yahoo.com


def key_to_compare(item):
    return item[1]

list_of_emails.sort(key=key_to_compare)
logger.info(list_of_emails)

# 24
list_of_machines = ["10.2.0.5/24", "10.2.0.3/24", "10.3.0.1/24"]
# sort it with host address . last digit

# logger.info("10.2.0.5/24".split("/")[0][-1])
list_of_machines.sort(key=lambda item: item.strip("/24")[-1])
logger.info(list_of_machines)


list_of_employees = [
    {"emp_id":34,
     "emp_name":"xx ab"},
    {"emp_id":2,
     "emp_name":"yy ca"},
    {"emp_id":1,
     "emp_name":"zz dc"}
]   # 34, 2, 1  # 1, 2, 34

# sort:
#     for item in list_of_employees:
#         key_to_compare(item)


def key_to_compare_dict(item):
    logger.info(item)
    return item['emp_id']

# list_of_employees
list_of_employees.sort(key=lambda emp_data: emp_data['emp_id'])
list_of_employees.sort(key=key_to_compare_dict)
logger.info(list_of_employees)


# need to sort with emp surname


# help(list_of_numbers.reverse)

# ===== reverse, copy in pending ============== #
list_of_numbers = [23,1, 45, 6,7]
logger.info(list_of_numbers[::-1])  # [7, 6, 45, 1, 23]
logger.info(list_of_numbers)      # [23, 1, 45, 6, 7]
list_of_numbers.reverse()         # [7, 6, 45, 1, 23]
logger.info(list_of_numbers)


# ================= Dictionary ===================
# 'copy',
# 'fromkeys',
# 'get','setdefault'
# 'items', 'keys', 'values'
# 'pop', 'popitem', 'clear',
# 'update'

logger.info(dir(dict))
list_of_keys =["emp_name","emp_id"]
# help(dict.fromkeys)
emp_data = dict.fromkeys(list_of_keys, None)
logger.info(emp_data)
logger.info(emp_data["emp_name"]) # value using key
# logger.info(emp_data["emp_address"])
logger.info(emp_data.get("emp_name"))
logger.info(emp_data.get("emp_address", "No Key Found"))
help(emp_data.get)
emp_data["emp_name"] = "xx"
logger.info(emp_data.get("emp_name"))

logger.info(emp_data.setdefault("emp_name"))  # emp_data.get("emp_name")
logger.info(emp_data.get("emp_address"))
logger.info(emp_data.setdefault("emp_address","12/A, India"))
logger.info(emp_data.get("emp_address"))
help(emp_data.setdefault)
#
emp_data["emp_name"] = "xx"
logger.info(emp_data.get("emp_name"))
logger.info(emp_data.setdefault("emp_name"))
logger.info(emp_data.setdefault("emp_phone",984502345))

# dict.keys() -> [key1, key2,...]
# dict.values() -> [ value1, value2,... ]
# dict.items() -> [ (key1, value1), (key2, value2) ...]
logger.info(emp_data.keys())
logger.info(emp_data.values())
logger.info(emp_data.items())

emp_data["emp_id"] = 1234
logger.info(emp_data.items())

# update emp_id using subscript method



new_data = {"emp_name":"new_xx", "emp_id":1234,"emp_dob":"12/05/1990"}

emp_data.update(new_data)
logger.info(emp_data)
logger.info(emp_data.pop("emp_id"))  # -> value of removed key   value
logger.info(emp_data)
logger.info(emp_data.popitem())  # (key, value)
# help(emp_data.popitem)
logger.info(emp_data)
emp_data.clear()
logger.info(emp_data)


# ================= set ========================= #
# 'copy',
# 'add'
# 'difference','symmetric_difference', 'intersection','union'
# 'update' , 'difference_update','intersection_update',  'symmetric_difference_update'
# 'isdisjoint',
# 'issubset', 'issuperset',
# 'pop', 'discard','remove', 'clear'

logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)
new_data_set = {23, 124, 123, 24}
# data_set.update(new_data_set)     # data_set = data_set + new_data_set
logger.info(data_set)
logger.info(data_set.difference(new_data_set))  # data_set - new_data_set
logger.info(data_set.intersection(new_data_set))  # data_set matches in new_data_set
logger.info(data_set.union(new_data_set))        # data_set + new_data_set
logger.info(data_set.symmetric_difference(new_data_set))  # data_set- new_data_set + (new_data_set - data-set)
#  data_section (not in intersection) + new_data_set (not in intersection) =
#
# data_set.update(new_data_set)
# logger.info(data_set)
# data_set.difference_update(new_data_set)  # data_set = data_set - new_data_set
# logger.info(data_set)
# data_set.intersection_update(new_data_set)  # data_set = intersection (data_set and new_data_set)
# logger.info(data_set)
# # data_set = Union(dataset and new_data_set) - Intersection(dataset and new_data_set)
# data_set.symmetric_difference_update(new_data_set)
#
# logger.info(data_set)
# #
# logger.info(data_set.issubset(new_data_set))
# logger.info(data_set.issuperset(new_data_set))
# logger.info(data_set.isdisjoint(new_data_set))
# #

logger.info({1,2,3}.issubset({1,2,3,4}))
logger.info({1,2,3,4}.issuperset({1,2,3}))
logger.info({30,40,60}.isdisjoint({1,2,3}))
# #
# set1 = {1, 2,3}
# set2 = {4, 5, 6}
# logger.info(set1.isdisjoint(set2))
#
# {123, 243}
logger.info(data_set.pop())  # retuns data
#help(data_set.pop)
# logger.info(data_set.remove(124))
#help(data_set.remove)
logger.info(data_set)
logger.info(data_set.discard(124))


# ==================== frozenset ================ #
#'copy',
# 'difference', 'intersection', 'union'
# 'isdisjoint', 'issubset', 'issuperset',
# 'symmetric_difference',
# logger.info(dir(frozenset))

logger.info(dir(frozenset))
fz = frozenset("python")
logger.info(fz)
fz = frozenset([1,2,3, 4,5,2])
logger.info(fz)





































