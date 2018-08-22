""" This module is to practise data types"""
# to comment out the code, select the line of code and ctrl + /
name = "python"
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
# #name[1] = 'e'
# #del name[0]
# #del name
# #print(name)
#
# # ======================= Mutable Modification and deletion data in Object ============ #
# list_of_accounts = [ 12345, 34556, 56789 ]
#
# print(list_of_accounts[0])
# list_of_accounts[0] = 23456
# print(list_of_accounts[0])
# del list_of_accounts[0]
# print(list_of_accounts)
#
# # ==================== Unordered data =============================== #
score_data = {"kohli": 199,
               "dhawan": 99,
               "dhoni": 49}

print(score_data)
print(score_data["kohli"])  # 199
del score_data["kohli"]
print(score_data)
print(score_data["dhawan"]) # 99







