""" To Practise OOPS concepts"""
from util.logger import get_logger
from weakref import WeakKeyDictionary


logger = get_logger()

a = 1
b = 20


class Voter:
    def __init__(self):
        self.req_age = 18
        self.age = WeakKeyDictionary()   # {82345:30}

    def __get__(self, instance_obj, objtype):
        logger.info(id(instance_obj))
        return self.age[instance_obj]

    def __set__(self, instance, new_age):
        logger.info(id(instance))
        if new_age < 18:
            msg = '{name} is too young to Vote in india'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        logger.info('{name} can Vote in India'.format(
            name=instance.name))
        logger.info(self.age)

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    voter_age = Voter()

    def __init__(self, name, age):
        self.name = name
        self.voter_age = age


p1 = Person('Miguel', 30)
logger.info(id(p1))
p2 = Person('Niki', 23)
logger.info(id(p2))
logger.info(p1.voter_age)
logger.info(p2.voter_age)

# account -> email
# email -> account

class Email:
    def __init__(self):
        # self.emails = {}   # {82345:30}
        self.emails = WeakKeyDictionary() # To avoid MemoryLeak

    def __get__(self, instance_obj, objtype):
        logger.info("Get Triggered for data descriptor")
        logger.info(id(instance_obj))
        return self.emails[instance_obj]

    def __set__(self, instance, new_email):
        logger.info("Set triggered for data descriptor")
        logger.info(id(instance))
        if "@" not in new_email :
            msg = '{} is not valid email'.format(new_email)
            raise RuntimeError("{} ".format(msg))
        self.emails[instance] = new_email
        logger.info(self.emails)

    def __delete__(self, instance):
        del self.emails[instance]

class Account:
    """ This is back account class """
    __data = 0
    no_of_account = 0
    email = Email()

    def __new__(cls, *args):
        logger.info("__new__")
        # logger.info(args)
        return object.__new__(cls)

    def __init__(self, account_name, account_number, account_phone, new_email):
        # self = temp_obj
        logger.info("init called {}".format(self))
        logger.info("{}, {} {}".format(account_name,account_number, account_phone))
        self.ac_name = account_name
        self.ac_number = account_number
        self.ac_phone = account_phone
        Account.no_of_account += 1
        self.email = new_email
        # Email.__set__(email, self, new_email)
        # email.__set__(Account_instance, new_email)

    def __len__(self):
        logger.info("Calling through len")
        return 1

    def get_account_number(self):
        logger.info(self.__name__)
        self.stream = "ECE"
        return self.ac_number

    def set_phone(self, new_number):
        self.ac_phone = new_number

    def set_email(self, new_email):
        if "@" in new_email:
            self.email = new_email

    def get_phone(self):
        logger.info(self.__class__)
        Account.validate_phone(self.ac_phone)
        return self.ac_phone

    def create_email(self, email):
        self.email = email

    @classmethod
    def get_no_of_accounts(cls, param2):
        # no_of_account = 2
        # logger.info(cls_name.__name__)
        logger.info(cls.no_of_account)
        pass

    @staticmethod
    def conn_db_session(param):
        logger.info("Connecting Db ")
        logger.info(param)
        pass

    @staticmethod
    def validate_phone(phone_num):
        pass

    def _set_acno(self, ac_no):
        self.ac_number = ac_no

    # def __del__(self):
    #     pass

Account.get_no_of_accounts(param2=30)
ac1 = Account("Naresh", 12344, 9108798743, "m2@1234.com") # object creation
# temp_obj = Account.__new__(Account, "Naresh", 12344, 9108798743)
# logger.info(temp_obj)
# temp_obj.__init__("Naresh", 12344, 9108798743)
#
# temp_obj2 = Account.__new__(Account, "Naresh", 12345, 9108798743)
# temp_obj2.__init__("Naresh",1234, 9108798743)
# temp_addr = __new__ # creating object
# temp_addr.__init__("Naresh", 12344, 9108798743)

ac2 = Account("xyz",2345, 7777777333, "test@gmail.com")   # object creation
#
logger.info(ac1.get_phone())
logger.info(ac2.get_phone())
logger.info(Account.get_phone(ac1))
logger.info(Account.get_phone(ac2))
# ac1.set_phone(123455556)
# logger.info(ac1.get_phone())
# logger.info(ac2.get_phone())
# logger.info(dir(ac1))


Account.get_no_of_accounts(40)
ac1.get_no_of_accounts(30)

# ac1.create_email("xyz@gmail.com")
# logger.info(ac1.email)
#
# ac2.create_email("yz@gmail.com")
# ac2.email

Account.conn_db_session(param=20)
ac1.get_no_of_accounts(param2=20)
# ac1.ac_number = 1234

ac1._set_acno(23456)
# ac1._Account__data

ac2.email = "m2-1234@gmail.com"
logger.info(ac2.email)
logger.info(ac2.email)
logger.info(ac1)
logger.info(ac2)
# del ac1
# del ac2
del ac1


class Machine:

    def __getattribute__(self, item):
        logger.info("__getattribute__ Calling")
        return object.__getattribute__(self,item)

    def __getattr__(self, item):
        logger.info("__getattr__ calling")

    def __setattr__(self, key, value):
        logger.info("__setattr__ calling")
        # object.__dict__[key] = value
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        logger.info("__delattr__ calling")

    def machine_date(self):
        logger.info("machine_date calling")

    def set_machine_date(self):
        logger.info("set_machine_date Calling")

    @property
    def machine_ip(self):
        logger.info("Calling machine ip")
        return self.ip

    @machine_ip.setter
    def machine_ip(self, new_ip):
        logger.info("Setting machine ip")
        self.ip = new_ip


m1 = Machine()
logger.info("machine_date() called")
m1.machine_date()  # -> __getattribute__ -> object.__getattrbite__(self, item) -> machine_date
# logger.info("machine ip called")
# m1.machine_ip()  # __getattribute__ -> object.__getattrbite__(self, item) -> raise AttributeError -> __getattr__()
logger.info("Setting machine name")
m1.name = "Windows machine"   # ->  __setattr__(self, key, value)
m1.name = "MacOS machine"
logger.info("Retrieving Machine name")
logger.info(m1.name)   # __getattribute__(self, item) -> object.__getattrbite__(self, item)

# logger.info(m1.machine_ip())
# m1.machine_ip("10.5.6.7")
m1.machine_ip = "10.5.6.7"
logger.info(m1.machine_ip)


# self.a = 1
# self. b =2
# {"a":1,
#  "b":2,
#  "name":"windows machine"}
# dict1 = {}
# dict1['name'] = "windows machine"
# dict1["name"]= "MacOS machine"

# @property
# def get_date():
#     return "Date"
#
# logger.info(get_date.getter)

class SampleClass:
    pass

class NewClass():
    pass

obj1 = SampleClass()  # refcount 1  # obj1 -> 0x02297370
obj2 = SampleClass()   # refcount 1
obj3 = SampleClass()   # refcount 1
obj4 = SampleClass()   # refcount 1
dict1 = {obj1:None, obj2:None}  # 0x02297370 refcount 2
logger.info(dict1)
del obj1     # 0x02297370 refcount 1
logger.info(dict1)

weakDict = WeakKeyDictionary()
# weakDict.update({"obj3":None})
weakDict[obj3]=None
weakDict[obj4]=None
del obj3
logger.info(list(weakDict.keys()))
del obj4
logger.info(list(weakDict.keys()))

#{<__main__.SampleClass object at 0x02297370>: None, <__main__.SampleClass object at 0x02297490>: None}
#{<__main__.SampleClass object at 0x02297370>: None, <__main__.SampleClass object at 0x02297490>: None}
#[<__main__.SampleClass object at 0x02297470>]
#[]

# obj1 -> obj2
# obj2 -> obj1
