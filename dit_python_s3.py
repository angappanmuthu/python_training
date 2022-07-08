
'''
Exception handling:
    try:
        ....
    except <exception>:
        ....
eg.
'''


from sklearn.model_selection import train_test_split
import imath

# import numpy as np
# from sklearn.model_selection import train_test_split

try:
    a = 2/0
except ZeroDivisionError:
    print("Zero Division Error")
except Exception as e:
    print(f'Exception : {e}')
finally:
    print('resource closed')

'''
user defined function

    def function_name():
        return value
    
    def function_name(arg1,arg2):
        return value

    def function_name():
        pass
'''


def draw_line():
    print("_____________________")


def add(x, y):          # function definition
    return x+y


def square(x):          # function definition
    return x**2


print("Function : addition -> ", add(1, 2))     # function calling
print("Function : square -> ", square(2))       # function calling


'''
    Python: 
        task 1: create function to register user.
        tast 2: create function to login user.
'''

users = list()


def register(username, password, email, phone):
    try:
        user = {"username": username, "password": password,
                "email": email, "phone": phone}
        users.append(user)
        return "Registration Success"
    except Exception as e:
        return f"Unable to register : {e}"


def login(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return "Valid User"
        else:
            return "Invalid User"


print(register("angappan", "232", "angappan@gamail.com", "23424"))
print(login("angappan", "232"))


'''
class and object

    class: blueprint of the object which is created. it has attributes (variables) and behaviors (functions)
    object: instance of the class.


    syntax for class:
        class <class_name>:
            pass

    syntax for object:
        <object_name> = <class_name>()

'''


class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth*self.length


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b)
print("Area of rectangle:", obj.area())

print()


# class Student(imath):
#     print("Student")


# print(Student(1, 2).add())


# Python code to demonstrate how parent constructors
# are called.

# parent class

class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
