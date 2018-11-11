from util.logger import get_logger
from logging import DEBUG

logger = get_logger()

# Defining function
# def function_name(parameters):
        # block of statements

# DEBUG , INFO , WARNING, CRITICAL, ERROR


def func_name():
    logger.info("Welcome to function")
    # return None
    # return


def sum_two(a, b): # required arguments
    logger.info("Sum of two is called")
    logger.info("Values passed a:%s b:%s", a , b)
    return a+b


# a b default c  1
def sum_three(a, b, c=1):  # a, b are required arguments, c is default argument
    logger.info("Sum of three called")
    logger.info("Values c=%s", c)
    result = a + b + c
    logger.info(result)
    return result, 1   #
    # return a + b + c

# sum_three(a, b)
# sum_three(a,b,c=20)
# sum_three(a,b) c=1

def sum_of_numbers(*args, **kwargs):
    logger.info("Variable length positional arugments: %s", args)
    logger.info("Variable length keyword arguments : %s", kwargs)


def new_func(arg, *args, **kwargs):
    logger.info("Required argument :%s",arg)
    logger.info("Variable length positional arugments: %s", args)
    logger.info("Variable length keyword arguments : %s", kwargs)


# data_list = []
# data_list = {"default_state':[]}
# data_list_deafault= []
# if data_list empty:
#    data_list = data_list_default
# else
#    data_list
# [20,30]
# [20,30,40]
# [2,3,60]
# [20,30,40,70]

# data_list_default - []  # 1234
# [].append(20)
# [20]

# [20,30].append(2)  # 2345
# [20,30]

def default_keyfunc(arg, data_list=[]):
    data_list.append(arg)
    return data_list


logger.info(func_name())
new_name = func_name
new_name()
logger.info(new_name.__name__)
logger.info(func_name.__name__)

logger.info(func_name())
logger.info(sum_two(12,13))

func_name()
sum_two(1, 2)  # (a, b) -> (a,b) = (1, 2)

sum_three(1, 2, 3)   # (a,b,c) = (1, 2, 3) a=1 b=2 c=3
sum_three(1,2)      # (a, b, c) = (1, 2, 1)  a=1 b=2 c=1

sum_two(b=2, a=1)
sum_three(c=20, b=3, a=2)

sum_two(1,b=3)   # (a, b) = (1, 3 )  => a=1, b =3
sum_three(1, c=30, b=20)  # (a, b, c) = (1,20, 30) -> a=1, b=20 c=30


sum_two(1, b=1)
sum_three(1, 2, c=20)

# sum_two(b=1, 1) # Error

# sum_three(1, c=20, 2) # Error

# sum_two(1,2,3)
# sum_two(a=1, b=2, c=3)
sum_of_numbers()  # positional and keywords empty
sum_of_numbers(1,2,3,4,5)   # *a = 1, 2,3, 4,5  -> a = (1,2,3, 4,5) # all positional arguments
sum_of_numbers(a=1, b=20, c=30)  # all keywords and empty positional
sum_of_numbers(1,2,3, c=30, d=20, a=20)  # 3 positional and 3 keywords
sum_of_numbers(1,2, c=40, value=40)

new_func(1)       # new_func(arg, *args, **kwargs) arg=1 args = () kwargs ={}
new_func(arg=20)  # arg=20  args=() kwargs={}
new_func(1,2,3)   # arg=1 args = (2,3)   kwargs = {}
new_func(a=1, b=20,c=30, arg=20)   # arg=20 args = () kwargs = {"a":1, "b":20, "c":30}
new_func(1,2,3,c=20, d=40)      # arg=1 args=(2,3) kwargs = {"c":20, "d":40}


logger.info(default_keyfunc(20))  # default_keyfunc(arg, data_list=[]) arg=20, data_list=[]
logger.info(default_keyfunc(30))   # arg=30 data_list=[] data_list.append(30) [20, 30]
logger.info(default_keyfunc(40))
logger.info(default_keyfunc(60, data_list=[2,3]))
logger.info(default_keyfunc(70))

logger.info(default_keyfunc.__code__)
logger.info(default_keyfunc.__dict__)
logger.info(dir(default_keyfunc))


