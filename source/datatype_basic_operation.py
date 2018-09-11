""" To practice basic operation"""
# ================== Numbers =============== #
# a = 2
# salary = 120034.24
#
# streaming_bit_octal = 0o12    # 10
# streaming_bit_hex = 0x12      # 18
# print(a)
# print(salary)
# print(streaming_bit_octal)
# print(streaming_bit_hex)
#
# # # ============= Strings ============== #
# message = 'Hello world'
# message2 = "Hello world"
#
# print(message)
# print(message2)
# print(message == message2)
#
# # Multi-line string
# message3 = """Hello
#             this is multi-line string.
#             used for Documenting functions, modules, classes
#             methods"""
#
# print(message3)
# #
# message4 = "Hello this is single line string , " \
#            "and it should not more than 120 " \
#            "characters in same line"
#
# print(message4)
#
# message5 = "Hello this is single line string , \nand it should not more than 120 \n" \
#            "characters in same line"
#
# print(message5)
# #
# # # ==================== List & Tuple ================== #
# list1 = [1, 20.2, "Python", [1, 3, 4]]
#
# tuple1 = (1, 20.2, "Python", [1, 3, 4])
#
# print(list1[0])
# list1[0] = 2345
# list1[2]
# print(list1)
# print(tuple1)
# print(type(list1))
# print(type(tuple1))
# del list1[1:2]
# print(list1)
# #
# # Use ',' if single data in tuple
# a = (1)
# print(a)  # 1
# print(type(a))  # <class 'int'>
# a = (1,)
# print(a)  # (1,)
# print(type(a))   # <class 'tuple'>
#
# # # =============== Dict & Set & Frozenset =============== #
# employee_id_data = {"xyz": 1,
#                     "mn": 2,
#                     "ll": 5,
#                     "mn": 12
#                     }
# print(list(employee_id_data))
# print(employee_id_data)
# print(type(employee_id_data))
# print(employee_id_data["xyz"])  # 1
# print(employee_id_data["mn"])  # 12
#
# employee_id_data["naresh"] = 1234
# print(employee_id_data)
# employee_id_data["naresh"] = 2435
# print(employee_id_data)
# del employee_id_data["xyz"]
# print(employee_id_data)
#
#
#
# unique_emplyee_set = {1, 2, 3, 1, 12 , 3}  # { 1, 2 ,3 , 12 }
#
# print(unique_emplyee_set)
# print(type(unique_emplyee_set))
#
# set_with_empty = {}
# print(type(set_with_empty))    # <class 'dict'>
#
# employee_data = frozenset(unique_emplyee_set)
# print(employee_data)
# print(type(employee_data))
#
# test_fz = frozenset("python")
# #print('p','y','t','h','o','n')
# print(test_fz)
#
# #list1 = ["python", 1, 2,3, 4.5,1]
# new_fz = frozenset(["python", 1, 2,3, 4.5,1])
# print(new_fz)
# frozenset({"python",1,2,3,4.5})
# #frozenset(1)
#
#
#
#
# # ===================== Basic operations ============ #
#
# print(4/2)    # 2.0
# print(4/2.0)  # 2.0
#
# print(4//2)   # 2
#
# print(2/3)
# print(2//3)
# print(9/4)  # 2.25
# print(9//4)  # 2
# print(9//4.0) # 2.0
#
#
# print(2**3)
#
# li = [2,3,4,5,6]
# for i in li:
#     print(i)
#
# for i in range(len(li)//2):  # [0:2:1] -> [0,1]
#     print(li[i])
#
#
# # sequential data type
# # [start: end: step]
# # [start=0:end=len(datetype):step=1]
# # [ start[0]: end[len(object): step[1] ]
#
# # [:] or [::]
# #  p   y    t   h   o   n
# #  0   1    2   3   4   5
# #  -6  -5  -4  -3  -2  -1
# name = "python"
# print(name[::])   # print(name[0:6:1])
#
# print(name[:])   # print(name[0:6:1])
#
# print(name[0:4])   # print(name[0:4:1])  # pyth
# print(name[:4])   # pyth
# print(name[::2])   # print(name[0:6:2]  # 0 , 2, 4  # pto
#
# list_of_message = ["welcome to python","welcome to java", "welcom to sql"]
# print(list_of_message[0][-4:-1])
#
# print(name[0]) # p
# print(name[2])  # t
# print(name[:])
# print(name[1:5])
# print(name[::])
#
# # for var in iteratable_object:
# #    print(var)
#
# for message in list_of_message:
#     print(message[-4:-1])
#
#
# message = "Hello how are you?"
# # how to reverse above message using slicing
# print(message[::-1])
# print(message[-1::-1])
#
#
# print("Hello "+"How are you")
# a = 20
# print("This is variable :"+str(a))
# print("This is variable :%s"%(a))
# print("This is variable :{}".format(a))
# print("This is variable :{var}".format(var=a))
#
# list1 = [1,2,3]
# list2 = [2,3,4,5]
# print(list1 + list2)  # list
# #list1 = list1 + list2   #  # O(n+k)
# list1.extend(list2)   # [1,2, 3, 2, 3,4, 5] # O(k)
# print(list1)
# # def extend(list2):
# #    for item in list2:
# #        list1.append(item)
# #    return None
# #  help dir
# help(list1.extend)
# tuple1 = (1,2,3)
# tuple2 = (2,3,4,5)
# print(tuple1 + tuple2)
#
# # Repetition
# print("*==="*12)    # "*===="+"*===="
# print("{form}Final Output{form}".format(form="="*12))
# print("Http Request status code:%s"%(200))
# print("="*12+"End Output"+"="*12)
# li1= ["msg1"]
# ["msg1","msg1"]
# print(li1* 10)
# print(li1)


list_lan = ["python", "java", "ruby", "scala", "R"]
list_lan[2] = "Ruby"
print(list_lan)
list_lan[3]="SCALA"
print(list_lan)

# del list_lan[1:2]
# print(list_lan)
# del list_lan[:]
# print(list_lan)

message = "Hello world"

message[::-1]  # [-1:-len(data)-1:-1]
message[4:3:-1]  # o  message[-6:-7:-1]   # 0
