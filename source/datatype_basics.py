""" This module is to practise data types"""
# to comment out the code, select the line of code and ctrl + /

# string represented in single(') or double(") or triple quotes(""")
name = "welcome to python"
name2 = 'welcome to python'
name3 = """welcome to python"""
name4 = """Triple quotes can also be used to
        write down multiline"""

name5 = "this will not " \
        "go to new line. This '\' coninuation line mark is " \
        "to avoid writing down more than " \
        "100 to 120 character in the same lin,"


# print(name)
# print(name[0])
# print(name[3])
# print(name[-1])
# print(name[5])
# print(name[-6])



# a = 20
# print(a)
# print(type(a))
# b = a
# print(b)
# print(type(b))
# b = 20

# print(id(a), id(b))
# print(a is b)
# #
# print("====== Changing the object for b ======")
# b = "python"
# print(a)
# print(b)
# print(type(b))
# print(id(a), id(b))
# print(a is b)
#
# # ================== Sequential data type ==================== #
name = "python example"
print(name)      # "python"
print(name[1])     # y
print(name[2])      # t
print(name[1], name[-5])  # y, a
print(name[4], name[-2])  # o, l
print("emptyCharacter:%s" % name[6])  #
print(name[7])    # e
listofnames = ["xyz","mn","zz"]
print(listofnames[1]) # "mn"
print(listofnames[2]) # "zz"

# # ===================Immutable Modification and deletion data not supported ============= #
# modification, addition, deletion of the specific element
# name[1] = 'e'
# del name[0]
#del name
# print(name)
#
# # ======================= Mutable Modification and deletion data in Object ============ #
list_of_accounts_list = [12345, 34556, 56789 ]
list_of_accounts_tuple = (12345, 34556, 56789)
INC = 0
ERROR_CODE = 500
STATUS_CODE = 200
list_of_const = (0, 500, 200)

#
print(list_of_accounts_list)
print(list_of_accounts_list[0])  # 12345
list_of_accounts_list[0] = 23456

# list_of_accounts_tuple[0] = 23456  #
print("tuple data",list_of_accounts_tuple[1])

print(list_of_accounts_list[0])
del list_of_accounts_list[0]
print(list_of_accounts_list)

a = 1  # integer
print(type(a))
a = ("xyz",)    # tuple unpacking  # a =1, b = 20
# a = "xyz"
print(type(a))  # integer
#
# # ==================== Unordered data =============================== #
# dict, set , fronzenset

# Key:value map
dict1 = {}  # this is dictionary
set1 = {1,2}
fz = frozenset([1,2, 3, 4, 1, 3, 45,"xx","xx"])
print(type(fz))
print(dir(set1))

print(dir)
for data in fz:
    print(data)

#
# read the data
# check the represenation
# retrieve the collection in the data
# if no data -> dict
# if data -> data is keys -> set

#
set1 = {"kohli", "dhawan","dhoni", "kohli", "dhoni"}
list1 = ["kohli", "dhawan","dhoni", "kohli", "dhoni"]
print(set1)  #
print(list1)


score_data = {"kohli": 199,  # 1
               "dhawan": 99,
               "dhoni": 49,
              "kohli":200}   # 1

print(score_data["kohli"])  # 200
print(score_data)
print(score_data)
print(score_data["kohli"])  # 199
del score_data["kohli"]
print(score_data)
print(score_data["dhawan"]) # 99
#
list_of_account = [
                    {
                        "name1":
                         {
                             "sbi_account":1234,
                            "icic account":2245
                         },
                    "name2":'123'
                     }
                    ]

previous_data = {"product1", "product2","product3"}
current_data = frozenset(["product8","product9"])
previous_data = previous_data.union(current_data)
print(previous_data)


current_month_set = {"product1", "product2", "product8", "product9"}
previous_month_set = {"product1", "product2", "product5"}








