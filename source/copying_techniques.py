""" This is for copying examples"""
import copy
import util

logger = util.logger.get_logger()


# list_of_data = [1234, 234, 456, 43]
list_of_data = [1234,234, 456,43, ["xx", "yy"]]
# new_data = list_of_data
# new_data = list_of_data.copy()  # shallow copy
new_data = copy.deepcopy(list_of_data)  # deep copy
new_data.append(100)
logger.info(list_of_data)
logger.info(new_data)
new_data[4].remove("yy")
logger.info(list_of_data)
logger.info(new_data)



# new_data_set = list_of_data.copy()

a = [1, 2, 3]
b = a[::]
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))

print(a is b)  # True
print(id(a) == id(b))
#
b[0] = 300  # [ 300, 2, 3]
print(a)
print(b)


# ================ Shallow Copy ================== #
a = [1, 2, 3, [20, 40]]
# b = copy.copy(a)
b = a[::]  # [start: end: increment] 0:len(seq)-1:1

print(id(a))
print(id(b))
# print(a[0] is b[0])  # True
print(a[3] is b[3])  # True
print(id(a[3]))
print(id(b[3]))
b[3][0] = 400
print(a)   # [1,2, 3, [400, 40] ]
print(b)   # [1,2,3, [400, 40] ]
# #
# # # ============== Deep Copy example ================== #
a = [1, 2, 3, [20, 40]]
b = copy.deepcopy(a)

print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
# print(a is b)
print(a[3] is b[3])   # False
b[3][0] = 400
print(a)
print(b)

#
# # ===================== Nested data in Immutable data type  =========== #
a = (1, 2, 3, [20, 40])
print(a)    # (1,2,3, [20, 40])
print(a[3])  # [20,40]
print(a[3][0])  # [20, 40][0] -> 20
a[3][0] = 300   # [20, 40 ][0] = 300 -> [300, 40]
print(a)        # (1, 2, 3, [300, 40])
# a[3] = 400      #  Error

# ====================== Copying Nested data in Immutable data type ===== #
a = (1, 2, 3, [20, 40])
b = a[:]
print(a)
print(b)
print(a is b)
print(a[3] is b[3])
b[3][0] = 300
print(a)
print(b)

a = (1, 2, 3, [20, 40])
b = copy.deepcopy(a)
print(a)
print(b)
print( a is b)
print(a[3] is b[3])
b[3][0] = 300
print(a)
print(b)

# b[3] = [20, 40]   #











