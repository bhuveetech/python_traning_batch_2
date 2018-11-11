from util.logger import get_logger

logger = get_logger()


class Person:

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def show_name(self):
        logger.info(self.name)

    def show_age(self):
        logger.info(self.age)

# p1 = Person("xyz", 22)
# p1.show_age()
# p1.show_name()

# definition of subclass starts here
class Student(Person):  # Person is the  superclass and Student is the subclass

    def __init__(self, student_name, student_age, student_id):
        Person.__init__(self, student_name,
                        student_age)  # Calling the superclass constructor and sending values of attributes.
        self.student_id = student_id

    def get_id(self):
        return self.student_id  # returns the value of student id


class Teacher(Person):

    def __init__(self, teacher_name, teacher_age, emp_id, subject):
        super(Teacher, self).__init__(teacher_name, teacher_age)
        self.emp_id = emp_id
        self.subject = subject

    def show_subject(self):
        return self.subject

# end of subclass definition


# Create an object of the superclass
person1 = Person("Richard", 23)
# call member methods of the objects
person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
logger.info(student1.get_id())
student1.show_name()

teacher1 = Teacher("Teacher1", 25,1234, "Maths")
teacher1.show_subject()
teacher1.show_name()
teacher1.show_age()


class A:

    def display(self):
        logger.info("Calling A")


class B:

    def display(self):
        logger.info("Calling B")


class C(A, B): # MRO Technique # Left to right # Depth first Search,

    def display(self):
        # A.display(self)
        logger.info("My Own implementation")


c1 = C()
c1.display()  # Search in C then A then B




# ================ slots ===================== #

class D:
    def __init__(self, data):
        self.value = data


d1 = D("Sample data")
d1.value2 = "Dynamic variable created"


logger.info(d1.__dict__)

d2 = D("D2 sample data")
logger.info(d2.__dict__)

class S:
    __slots__ = ["value"]

    def __init__(self, data):
        self.value = data

s1 = S("Sample Data")
# s1.value2 = "Dynamica variable created"

s2 = S("S2 sample data")

# logger.info(s1.__dict__)
# logger.info(s2.__dict__)
logger.info(s1.__slots__)
logger.info(s1.value)
logger.info(s2.value)


