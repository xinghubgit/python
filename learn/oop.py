#Python is a multi-paradigm programming language. It supports different programming approaches.
#The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

#These attributes are defined inside the __init__ method of the class. It is the initializer method that is first run as soon as the object is created.
#Class
#Object
#Inheritance
#Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
#Encapsulation
#Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
# Polymorphism
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).


# Key Points to Remember:
# Object-Oriented Programming makes the program easy to understand as well as efficient.
# Since the class is sharable, the code can be reused.
# Data is safe and secure with data abstraction.
# Polymorphism allows the same interface for different objects, so programmers can write efficient code.

#The first string inside the class is called docstring and has a brief description about the class. Although not mandatory, this is highly recommended.
#A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.

#You may have noticed the self parameter in function definition inside the class but we called the method simply as harry.greet() without any arguments. It still worked.
#This is because, whenever an object calls its method, the object itself is passed as the first argument. So, harry.greet() translates into Person.greet(harry).
#In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method's object before the first argument.

#Class functions that begin with double underscore __ are called special functions as they have special meaning.
#An interesting thing to note in the above step is that attributes of an object can be created on the fly. We created a new attribute attr for object num2 and read it as well. But this does not create that attribute for object num1.

#Inheritance enables us to define a class that takes all the functionality from a parent class and allows us to add more. In this tutorial, you will learn to use inheritance in Python.
#Two built-in functions isinstance() and issubclass() are used to check inheritances.

#Python Multiple Inheritance
#A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.
#In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.
#So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

#Python operators work for built-in classes. But the same operator behaves differently with different types. For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
#https://docs.python.org/3/reference/datamodel.html#special-method-names

#Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)
print(my_iter.__next__())
print(next(my_iter))

#We use the next() function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception. Following is an example.

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

number = PowTwo(4)
for i in number:
    print(i)
generator = (x ** 2 for x in my_list )
for i in generator:
    print(i)

