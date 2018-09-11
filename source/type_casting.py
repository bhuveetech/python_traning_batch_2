""" To Practise Type casting operation"""
import logging

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


# list_of_fruits = ["apple","banana", "orange"]
# input_value = input("Enter some number: ")
# logger.debug(type(input_value))
# logger.debug(input_value)
# int_value = int(input_value)
# logger.debug(type(int_value))
# logger.debug(list_of_fruits[int_value])
#
# #int("2.34")
# logger.debug(int("0o1", base=8))
# logger.debug(int(2.34))
# logger.debug(int(0o1))
#
# # log.debug(help(int))
#
#
# print("The given value is :"+ input_value)
# logger.debug("The given value is :"+ str(int_value))

class_information = [
    {"name":"xyz",
     "dob":"13/07/2017"},
    {"name":"yz",
     "dob":"12/05/2017"}
]

new_tuple = tuple(class_information)
logger.debug(type(new_tuple))
logger.debug(new_tuple)

# list(1)


logger.debug("2nd Class information :"+ str(class_information))
debug_message= "2nd class information:%s"%(class_information)
debug_message2 = "2nd class information:a {b}".format(a=10, b=20)
debug_message3 = "{cls}nd class information".format(cls=2)
debug_message4 = "{class_id} information".format(class_id="2nd")
debug_message5 = "{} information {}".format("2nd",class_information)
logger.debug(debug_message)
logger.debug(debug_message2)
logger.debug(debug_message3)
logger.debug(debug_message4)
logger.debug(debug_message5)
logger.debug(debug_message2)


message = "python"
logger.info(message)
logger.info(list(message))  # list(iterable) tuple(iterable) set(iterable) frozenset(iterable)

# {1:"xx", 2:"yy"}

logger.info(list(class_information[0]))

d = dict(name="xyz",dob="13/07/2017")
logger.info(d)

d1 = dict(zip(("name","dob"),("xyz","13/07/2017")))
logger.info(d1)


d = dict([("name","xyz"), ("dob","13/07/2017")])
logger.info(d)




