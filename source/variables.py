"""Variables practise"""
# alt + insert -> to see option for module creation
# shift + alt + f10  -> to see execution option
# shift + f10  -> to return the previous executed file

emp_name = "xyz"  # string
emp_id = 1234     # integer
emp_email = "xyz@gmail.com"  # string
emp_salary = 23456.77   # float
emp_address = "22/A, Street road " \
              "Hyderabad India"
emp_phone = 98222234555

system_ip = "10.3.4.5"

print(emp_name, emp_phone, emp_id)

emp_name = "yzm"

print(emp_name)  # yzm

a = 10
b = 10
print(a, b)  # 10, 10
b = 20
print(a, b)  # 10, 20


# # Unsupported
# db_name =
#
# Three variables assigned to same value
a = b = c = 1
print(a)
print(b)
print(c)

# id retuns address of the given object
print(id(a), id(b), id(c))   # id
#
# Three variables to different data
a, b, c = 1, 20.23, "python"
print(a)
print(b)
print(c)
print(id(a), id(b), id(c))
#
# Multiple statements in Single Line but not recommended by PEP8
a = 1; b = 3; c = 3456; print(a, b, c)






