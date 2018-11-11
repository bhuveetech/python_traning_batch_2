from util.logger import get_logger
from abc import ABCMeta, abstractmethod
# =================== Overriding ===================== #

# Overriding, Overloading,

logger = get_logger()

# abstractmethod ->


class Animal(metaclass=ABCMeta):

    def __init__(self, name):    # Constructor of the class
        self.name = name

    @abstractmethod
    def talk(self):
        pass

    def show_animal_name(self):
        logger.info(self.name)


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    # pass
    def talk(self):
        return 'Woof! Woof!'

    def cal(self, num, num1=None, num2=None):
        logger.info("Calling")

    # def cal(self, float num, num2):
    #     logger.info("Calling")


cat1 = Cat('Missy')
cat2 = Cat('Mickey')
dog1= Dog('Lassie')
logger.info(cat1.talk())
logger.info(cat2.talk())
logger.info(dog1.talk())


# Using default keyword
class sum1:
    # def cal_sum(self,x,y):
    #     return x+y

    def cal_sum(self,x, y, z=0):
        return x + y + z



ob = sum1()
logger.info(ob.cal_sum(10, 20))
logger.info(ob.cal_sum(20,30, 40))

# Using variable length argument
class sum:
    def sum(x, y, *arg):
        return x + y + sum(arg)

ob = sum1()
logger.info(ob.cal_sum(10, 20))
logger.info(ob.cal_sum(20,30, 40))


# Operator overloading

class A:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value + other.value)

    def show_value(self):
        return self.value


a1 = A(1)
a2 = A(2)
# a3 = A(3)
a3 = a1 + a2
logger.info(a3.show_value())


logger.info(issubclass(sum, (Animal)))
help(issubclass)

# issubclass()
logger.info(isinstance(a1, A))
logger.info(hasattr(a3,"value"))
help(hasattr)
setattr(a3, "value",3)
logger.info(getattr(a3, "value"))
delattr(a3, "value")

# logger.info(a3.value)