from util import logger as log
import pandas as pd  # This module used for data analytics and science
# from fabric.operations import prompt
# import xlrd   # read data from xl sheet
#
# import MySQL-python
# import mysqlclient


logger = log.get_logger()
store_data = pd.read_excel("..\config\sample_superstore.xls")
# logger.info(store_data)
# logger.info(dir(store_data))
# if store_data:
#     logger.info(store_data.values)

# 0,and  All empty data types, and None object considered as False
# else True

logger.info(type(store_data))
profit = store_data['Profit']
product_name_data = store_data["Product Name"]

logger.info(profit)
if not store_data.empty:
    logger.info("Data is loaded ")

else:
    logger.error("No data present")


#
# for profit_value in profit:
#     logger.info(profit_value)
#     if profit_value < 0:
#         continue
#         logger.info("It's loss")
#         # break
#
#     elif 0 < profit_value < 50:
#         logger.info("It's Average profit")
#
#     elif 50 <= profit_value < 100:
#         logger.info(("Mariginal profit"))
#
#     else:
#         logger.info("More profit")
#
#
# else:  # when no break statement executed in the loop
#     logger.info("No break statement found")
name = ("name", "xyz")
logger.info(name)
key, value = ("name", "xyz")
logger.info("%s , %s", key, value)
list1 = ["name","id"]
list2 = ["xyz", 1234]
data  = zip(list1, list2) # [("name","xyz"), ("id", 1234) ]
for key, value in data:
    logger.info("%s: %s", key, value)

list_of_products = []
for product_name, profit_value in zip(product_name_data, profit):
    if profit_value > 0:
        list_of_products.append(product_name)

logger.info("List of the profit products:%s",list_of_products)

profit_product_comprehension = [product_name
                           for product_name, profit_value in zip(product_name_data, profit)
                           if profit_value > 0]

logger.info(profit_product_comprehension)
logger.info(list_of_products == profit_product_comprehension)

logger.info("Store data analysis is done....")

#
# people_age = [21, 18, 17, 23, 24]
# #
# for age in people_age:
#     if age > 18:
#         continue
#
#     logger.info("Create a voter Id")
    # create_voterid()

# logger.info(dir(MySQLdb))
# con = MySQLDb.conn(host="", user="",pwd="", db="")
# pd.read_sql("select *from testable;", conn=con, )

# logger.info(help(prompt))

# logger.info("=============== ATM Application ============== #")
# logger.info("Insert your card")
# logger.info("Enter your password:")
# pass_word = input()
# # Get Card password from db
# # To validate the entered password
# # Get card account details and balance from db
# balance = 20000
#
# while True:  # while True/False
#     logger.info("Enter option to continue")
#     logger.info("1.Withdraw\t2.Balance Check")
#     option = int(input())
#     if option == 1:
#         logger.info("Enter amount to Withdraw:")
#         withdraw_amount = int(input())
#         if withdraw_amount <= balance:
#             balance = balance - withdraw_amount
#             # update balance amount in db
#             logger.info("Collect Amount: %s", withdraw_amount)
#
#         else:
#             logger.warning("You entered amount more than available balance")
#             continue
#
#     elif option == 2:
#         # Get balance from db
#         logger.info(balance)
#
#     else:
#         logger.info("You have selected wrong option, Try again")
#         continue
#
#     logger.info("Do you want to continue y/n")
#     continue_option = input()
#     if continue_option == "n":
#         break


# list comprehension
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_odd = []
for num in list_of_numbers:
    if num % 2:  # num % 2 ! =0
        list_of_odd.append(num)

logger.info("Filtered list:%s",list_of_odd)

list_of_odd = [num for num in list_of_numbers if num % 2] # no else support
logger.info(list_of_odd)

list_of_even = [num for num in list_of_numbers if not(num % 2)]  # num % 2 == 0
logger.info(list_of_even)

list_of_odd_gen = (num for num in list_of_numbers if num % 2)

logger.info(list_of_odd_gen)
# logger.info(list_of_odd_gen.__next__())
# logger.info(list_of_odd_gen.__next__())

for val in list_of_odd:
    logger.info(val)

for val in list_of_odd:
    logger.info(val)

for gen_val in list_of_odd_gen:
    logger.info(gen_val)


def gen_data(i):
    return 1*i


# range, xrange    # range(10) -> [0,1,2,3,4,5,6,7,8,9]
# xrange(10) -> generator object

# range -> generator

logger.info(range(10))
for time in range(10):
    logger.info(time)


# dict comprehension
# set comprehension


dict_com = {product_name:profit_value for product_name, profit_value in zip(product_name_data, profit)
            if profit_value > 0}
logger.info(dict_com)

set_com = {product_name for product_name, profit_value in zip(product_name_data, profit)
            if profit_value > 0}
logger.info(dict_com)
logger.info(set_com)

# [start:end:step] # range(0,10,1) #






