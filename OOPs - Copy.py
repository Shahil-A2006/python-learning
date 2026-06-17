"""       OOPs - object oriented programming          """


#   OOPs is the one of the most widely used programming paradigm (paradigm is the different ways for solution).
#   OOPs is organizing with using of Object & Class.

# class student:
#     name="shahil"
#     age=20

# s1=student()
# print(s1.name)
# print(s1.age)


# ============================================================================================


# class Human:
#     name="Shahil"
#     age=20

#     def greet(self):
#         print("Hello I am",self.name,".I am",self.age," years old boy")

# hi=Human()
# hi.greet()
# print(hi.name)
# print(hi.age)

# ============================================================================================

"CONSTRUCTER"

# A constructer is a special method in a class that is automatically called when an object of the class is created.
#it is used to initialize the attribute of the object.
# in python the constructer method is defined using __init__().

#eg:

# class Person:
#     def __init__(self,name,age,gender):
#         self.name1=name
#         self.age1=age
#         self.gender1=gender
#         print(self.name1)
#         print("constructor working")

#     def display(self1):
#         print("*************")
#         print("Name:",self1.name1)
#         print("Age:",self1.age1)
#         print("gender:",self1.gender1)

#     def show(self):
#         print("My name is",self.name1,"and i am",self.age1,"years old")

# p1=Person("shahil",20,"Male")

# p1.display()

# print(p1.age1)


# ============================================================================================


"""DISTRUCTER"""

# A distructor is a special method in a class that is automatically called when an object of the class is destroyed.
# in pyhton the distructor method is defined using __del__().

#eg:
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __del__(self):
#         print("distructer worked")

#     def display(self):
#         print(self.name)
#         print(self.age)

# p1=person("amal",30)

# del p1     #error(name 'p1' is not defined) bcoz here delete the object

# p1.display()



"""   INHERITANCE   """

# inheritance is way of creating new classes based on existing classess
# it allows to reuse the code from the parent class in the child class
# The child class inherits the attributes and methods from the parent class.

# eg:


# class Animal:                           #parent class
#     def sound(self):                    #parent method
#         print('the animal make sound')

# class Dog(Animal):                      #child class
#     def bark(self):                     #child method
#         print('the dog barking')

# x=Dog()
# x.sound()           #can call parent method with child object
# x.bark()



"""Types of Inheritance"""

""" 1. single inheritance : A child class inheritance from a single parent class"""

# class Dad:
#     def bike(self):
#         print('ride bullet')
# class Son(Dad):
#     def car(self):
#         print('ride alto')

# x=Son()
# x.bike()
# x.car()

# ----------------------------------------------------------------------------------------------
############## single inheritance with parameters  #################
# ----------------------------------------------------------------------------------------------

# class parent:
#     def parent_method(self,a):
#         self.A=a
#         print("hello guys",a)

# class child(parent):
#     def child_method(self):
#         print("hai friends",self.A)

# c=child()
# c.parent_method('i am shahil')
# c.child_method()


# ----------------------------------------------------------------------------------------------
############## single inheritance with parameters and accessing the parent class constructor in child class  ########
# ----------------------------------------------------------------------------------------------

# class parent:
#     def __init__(self,a):
#         self.b=a
#         print("from parent")

#     def parent_method(self):
#         print("This is the parent method",self.b)

# class child(parent):
#     def child_method(self):
#         print("This is the child method",self.b)

# c=child("HELLO")
# c.parent_method()
# c.child_method()


# ----------------------------------------------------------------------------------------------
############## single inheritance with both child and parent class have constructer  #################
# ----------------------------------------------------------------------------------------------

# class parent:
#     def __init__(self):
#         print("parent class")
#     def show(self):
#         print("parent class")

# class child(parent):
#     def __init__(self):
#         print("child class")
#         super().__init__()
#     def show(self):
#         print("child class")
    
# ob=child()


# ----------------------------------------------------------------------------------------------
############## single inheritance with both child and parent class have constructer  ###########
# ----------------------------------------------------------------------------------------------

# class parent:
#     def __init__(self,a):
#         self.B=a
#         print('from parent class')

#     def show(self):
#         print("from parent class",self.B)

# class child(parent):
#     def __init__(self,a,b):
#         self.A=a
#         print("from child class")
#         super().__init__(b)

#     def show1(self):
#         print("from child class",self.B,self.A)

# obj=child("hello","hai")
# obj.show()
# obj.show1()


#.......................................with same method name in both parent and child

# class Parent:
#     def __init__(self,b):
#         self.x=b
#         print('parent constructor')
#     def method(self):
#         print('parent method',self.x)
# class Child(Parent):
#     def __init__(self,a,b):
#         self.y=a
#         print('child constructor')
#         super().__init__(b)                     #calls constructor in parent
#     def method(self):
#         print('child method',self.y,self.x)
#         super().method()                        #calls the method from parent

# x=Child('hello','hai')
# x.method()


"""multiple inheritance"""


# class Parent1:                  #parent class
#     def par1(self):
#         print('parent 1 method')
# class Parent2:                  #parent class
#     def par2(self):
#         print('parent 2 method')
# class child(Parent1,Parent2):                    #child class
#     def chil(self):
#         print('child method')


# obj=child()
# obj.par1()
# obj.par2()
# obj.chil()


"""multiple inheritance with construtor in child and both parents"""
# class Parent1:                  #parent class
#     def __init__(self):             #parent1 constructor
#         print("parent 1 constructor working")
#     def par1(self):
#         print('parent 1 method')
# class Parent2:                  #parent class
#     def __init__(self):             #parent 2 constructor
#         print("parent 2 constructor working")
#     def par2(self):
#         print('parent 2 method')
# class child(Parent1,Parent2):                    #child class
#     def __init__(self):                            #child constructor
#         print("child constructor working")
#         super().__init__()                  #to call parent1 constructor
#         Parent2.__init__(self)                 #to call parent2 constructor
#     def chil(self):
#         print('child method')
    

# obj=child()
# print(child.mro()) #=> to show the python search path for methods/constructor

"""MRO - Method Resolution Order"""
# MRO is a mechanism / method in python
# it returns the order in which python such classes for methods and attributes during inheritance
# The MRO is a list of classes in the order in which they are searched when a method is called
# The first class in the list is the immediate parent class and the last class in the list is the most derived class
# The MRO is used to resolve method calls in python , and it is important to undersdtand how it works to avois unexpected behaviour


"""multi level inheritance"""
# class Parent:  
#     def par(self):
#         print('parent method')
# class Child(Parent):
#     def chi(self):
#         print('child method')
# class Grand_child(Child):
#     def grachi(self):
#         print('grand child method')

# ob= Grand_child()
# ob.grachi()
# ob.chi()
# ob.par()

"""multi level inheritance with constructor in all class"""
class Parent:                           #parent class
    def __init__(self):                 #parent constructor
        print('parent constructor')
    def par(self):
        print('parent class method')
class Child(Parent):                    #child class
    def __init__(self):                     #child constructor
        print('child constructor')
    def chi(self):
        print('child class method')
class Grand_child(Child):               #grand child class
    def __init__(self):                     #grand child constructor 
        print('grand child constructor')
        super().__init__()                  #calling parent class method
        Parent.__init__(self)               #calling grand parent method (also can call with super() in parent class)
    def grachi(self):
        print('grand child class method')

x=Grand_child()
x.grachi()
x.chi()
x.par()


"""hierarchical inheritance"""

"""When more than one derived classes are created from a single base class , zthis type of
   inheritance is called hierarchial inheritance"""
"""in this type of inheritance , multiple child classes inherit from a single parent class"""

# class Parent:               #parent class
#     def par_method(self):
#         print('parent method')

# class Son(Parent):              #first child class
#     def son_method(self):
#         print('son method')
# class Daughter(Parent):         #second child class
#     def dau_method(self):
#         print('daughter method')

# x1=Son()
# x1.son_method()
# x1.par_method()

# x2=Daughter()
# x2.dau_method()
# x2.par_method()


"""hierarchical inheritance with constructor in all class"""

class Parent:               #parent class
    def __init__(self):         #parent constructor
        print('parent constructor')
    def par_method(self):
        print('parent method')

class Son(Parent):              #first child class
    def __init__(self):         #first child constructor
        print('son constructor')
    def son_method(self):
        print('son method')
class Daughter(Parent):         #second child class
    def __init__(self):             #second child constructor
        print('daughter constructor')
    def dau_method(self):
        print('daughter method')

x1=Son()
x1.son_method()
x1.par_method()

x2=Daughter()
x2.dau_method()
x2.par_method()


"""Hybrid Inheritance"""

# inheritance consisting of multiplle type of inheritance is called Hybrid inheritance.


# class School:
#     def school_meth(self):
#         print('school method')
# class Teacher1(School):r
#     def t1_meth(self):
#         print('teacher-1 method')
# class Teacher2(School):
#     def t2_meth(self):
#         print('tecaher-2 method')
# class Student1(Teacher1,Teacher2):
#     def stu1_meth(self):
#         print('student-1 method')
# class Student2(Teacher1):
#     def stu2_meth(self):
#         print('student-2 method')
"""
school-techer1 / school-teacher2/ teacher1-student2  => single inheritance
teacher1 & teacher2- student1 => multiple inheritance
school- teacher1- student2 => multilevel inheritance
school-techer1 & teacher2 => hierarchical inheritnace
"""



"""DATA ABSTRACTION"""

# data abstraction- is the process of hiding behind operations. only showing essential features.
# from abc import ABC,abstractmethod
# abc- module which contain ABC, abstraction
# ABC- abstract class



# from abc import ABC,abstractmethod              #importing abstract class and abstract method from 'abc' module
# class Vehicle(ABC):                 #abstract class (inherit from ABC)
#     @abstractmethod                 #abstract method(using decorator)
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):                                         #derived class
#     def start(self):
#         print('car starts by turning key or ignition switch')
#     def stop(self):
#         print('car stops by swicth or turning key')
# class Bike(Vehicle):                                        #derived class
#     def start(self):
#         print('bike starts by self start switch or kick start')
#     def stop(self):
#         print('bike stops by swicth or turning key')

# x=Car()
# x.start()
# x.stop()

# y=Bike()
# y.start()
# y.stop()




"""polymorphisum"""
# class parent:
#     def a(self):
#         print('hi')
# class Child(parent):
#     def a(self):
#         print('hello')

# x=parent()
# x.a()                 #calls parent method
# y=Child()
# y.a()                 #calls child method (both a() gives different output)


"""method-overriding"""
# class parent:
#     def a(self):
#         print('hi')
# class Child(parent):
#     def a(self):
#         print('hello')

# x=Child()
# x.a()           #same method name in parent and child class


"""method-overloading"""
# class Person:
#     def a(self,name,place=None):
#         print(name,place)

# x=Person()
# x.a('anu')
# x.a('anu','calicut')   #to overcome override, need to set default value/None to the parameters.








