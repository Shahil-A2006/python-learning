"""1.Define a class Rectangle with attributes length and width. Write methods to calculate:
* The area of the rectangle.
* The perimeter of the rectangle."""
# class Rectangle:
#     def area(self,length,width):
#         self.a=length
#         self.b=width
#         print(f'area of the reactangle is: {self.a*self.b}')
#     def peri(self):
#         print(f'perimeter of the reactangle is : {(self.a+self.b)*2}')

# x=int(input('enter length of the reactangle: '))
# y=int(input('enter width of the reactangle: '))
# w=Rectangle()
# w.area(x,y)
# w.peri()


"""2.Create a class Person with attributes first_name and last_name. Write a method full_name that returns the person's full name."""
# class Person:
#     def full_name(self,first_name, last_name):
#         print(f"full name is : {first_name+' '+ last_name}")

# x=input('enter first name: ')
# y=input('enter last name: ')
# w=Person()
# w.full_name(x,y)


"""3.Create a class Laptop with attributes brand, model, and price. Write a method discounted_price that takes a discount percentage and returns the price after applying the discount."""
# class Laptop:
#     def discounted_price(self,brand,model,price):
#         disc=int(input('enter discount percentage: '))
#         import math
#         final_price=math.floor((price-((disc/100)*price)))
#         print(f"the final price of the {brand+ model} is {final_price}")

# com=input('enter the brand name: ')
# mod=input('enter the model: ')
# pri=int(input('enter the price: '))
# lptp=Laptop()
# lptp.discounted_price(com,mod,pri)


"""4.Write a class Student with attributes name and roll_number. Create two objects of the class and print their attributes."""
# class Student:
#     def detail(self,x,y):
#         print(f'student name : {x} with roll number: {y}')

# s1=Student()
# s2=Student()
# s1.detail('abhi','01')
# s2.detail('yasir','02')


"""5.Create a class Pen with attributes color and brand. Write a method write that prints "Writing with a [color] pen of [brand]."""
# class Pen:
#     def spec(self,color,brand):
#         print(f"Writing with a {color} pen of {brand}")

# obj=Pen()
# obj.spec('red','parker')


"""6.Write a class Car with attributes brand and color. Create two objects of this class and print their details."""
# class Car:
#     def spec(self,color,brand):
#         print(f"that is a {color+' '+brand}")

# obj=Car()
# obj.spec('red','BMW')


"""7.Create a class Student with attributes name and age. Use _init_ to initialize them. Create an object and print the details."""
# class Student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def stu(self):
#         print(f'student {self.name} is {self.age} year old')

# s1=Student('abhinand',30)
# s1.stu()


"""8.Define a class Dog with attributes name and breed. Add a method bark() that prints "Woof! I am <name>". Create an object and call the method."""
# class Dog:
#     def bark(self, name, breed):
#         print(f'Woof! I am {name}')
# pet=Dog()
# pet.bark('toby','pitbull')

"""9.Create a class Book with attributes title and author. Create three objects of this class with different values and display their details."""
# class Book:
#     def det(self,title,author):
#         print(f'{author} is the author of {title}')

# b1=Book()
# b1.det('pathummante aadu','basheer')
# b2=Book()
# b2.det('kayar','thakazhi')
# b3=Book()
# b3.det('chemmeen','thakazhi')


"""10.Write a class Employee with a class variable company = "Google" and an instance variable name. Show how changing name affects only that object but company is shared."""
# class Employee:
#     company='google'
#     def det(self,employ):
#         self.e=employ
#         print(f'{self.e} is the employee of {self.company}')

# p1=Employee()
# p1.det('abhinand')

"""11.Write a class Laptop with attributes brand and price. Create an object, then update the price of that object and display the updated details."""
# class Laptop:
#     def det(self,brand, price):
#         print(f"{brand} is starting from {price}")

# l1=Laptop()
# l1.det('dell','40000')

"""12.Create a class Calculator with a method add(self, x, y) that returns the sum. Create an object and use it to add two numbers."""
# class Calculator:
#     def op(self,x,y):
#         print(f'the sum of the numbers is {x+y}')

# a=int(input('enter first no: '))
# b=int(input('enter second no: '))
# c=Calculator()
# c.op(a,b)

"""13.Create a class Person with attributes name and age. Create an object and then delete it using del. Try printing it after deletion."""
# class Person:
#     def det(self, name, age):
#         print(name,age)

# p1=Person()
# del p1
# p1.det('abhi','30')

"""14.Create a class Mobile with attributes brand and ram (default "4GB"). Show how default values work when creating objects."""
# class Mobile:
#     def spec(self,brand,ram=4):
#         print(f'the {brand} having {ram}Gb Ram')

# m1=Mobile()
# m1.spec('vivo',8)
# m2=Mobile()
# m2.spec('mi')


"""15.Write a class BankAccount with methods:
deposit(amount)
withdraw(amount)
display_balance()"""
# class Bankacct:
#     def depo(self,bal,dep):
#         print(f'account balance is : {bal}')
#         print(f' after deposite the balance is : {dep+bal}')
#     def witd(self,bal,wit):
#         print(f'account balance is : {bal}')
#         print(f' after withdraw {wit} balance is : {bal-wit}')

# bal=int(input('enter balance amount: '))

# # dep=int(input('enter deposite amount: '))
# # c1=Bankacct()
# # c1.depo(bal,dep)

# wit=int(input('enter withdraw amount: '))
# c2=Bankacct()
# c2.witd(bal,wit)


"""16.Create an account and perform some deposits/withdrawals."""
# class Bankacct:
#     def __init__(self,bal,dep,wit):
#         self.b=bal
#         self.d=dep
#         self.w=wit
#     def depo(self):
#         print(f'account balance is : {self.b}')
#         self.b+=self.d
#         print(f' after deposite {self.d}, the balance is : {self.b}')
#     def witd(self):
#         print(f'account balance is : {self.b}')
#         self.b-=self.w
#         print(f' after withdraw {self.w}, balance is : {self.b}')


# bal=int(input('enter balance amount: '))
# dep=int(input('enter deposite amount: '))
# wit=int(input('enter withdraw amount: '))

# c1=Bankacct(bal,dep,wit)
# c1.depo()
# c1.witd()

"""........................................single inheritance........................................................."""

"""1. Create a parent class Person with a method display() that prints "I am a person".
Create a child class Student that inherits from Person and has a method study() that prints "I am studying".
Create an object of Student and call both methods."""
# class Person:
#     def display(self):
#         print('I am a person')
# class Student(Person):
#     def Study(self):
#         print('I am studying')

# p1=Student()
# p1.display()
# p1.Study()


"""2.Create a parent class Bank with method deposit() that prints "Deposit successful".
Create a child class Account with method balance() that prints "Balance updated".
Create an object of Account and call both methods."""
# class Bank:
#     def deposit(self):
#         print('deposit successful')
# class Account(Bank):
#     def balance(self):
#         print('balance updated')

# x=Account()
# x.deposit()
# x.balance()


"""3.Create a parent class Student with attributes name and rollno.
Create a child class Marks that adds attributes maths and science and a method display() to print all details."""
# class Student:
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
# class Marks(Student):
#     def display(self,maths,science):
#         print(f'the student {self.n} with roll number {self.r} obtained {maths} marks in maths and {science} marks in science')

# s1=Marks('raju',12)
# s1.display(48,56)


"""4.Create a parent class Mobile with method call().
Create a child class Smartphone with method internet().
Show how the child can access both methods."""
# class Mobile:
#     def call(self):
#         print('redmi')
# class Smartphone(Mobile):
#     def internet(self):
#         print('5G')

# x=Smartphone()
# x.internet()
# x.call()


"""5.Create a parent class Fruit with method taste().
Create a child class Mango with method color().
Call both methods using the Mango object."""
# class Fruit:
#     def taste(self):
#         print('is sweet')
# class Mango(Fruit):
#     def color(self):
#         print('alphonsa')

# x=Mango()
# x.color()
# x.taste()


"""6.Create a parent class Employee with method work().
Create a child class Manager with method manage().
Call both methods using the Manager object."""
# class Employee:
#     def work(self):
#         print('employee')
# class Manager(Employee):
#     def manage(self):
#         print('manager')

# x=Manager()
# x.manage()
# x.work()


"""7.Create a parent class Bird with method fly().
Create a child class Parrot with method talk().
Call both methods using the Parrot object."""
# class Bird:
#     def fly(self):
#         print('bird fly')
# class Parrot(Bird):
#     def talk(self):
#         print('parrtot talk')

# x=Parrot()
# x.talk()
# x.fly()



"""1. Write a program where Employee is a base class with name and salary.
 Derive a Manager class that adds department and a method to display all details."""
# class Employee:
#     def __init__(self, name, salary):
#         self.n=name
#         self.s=salary
# class Manager(Employee):
#     def dep(self, department):
#         print(f'employee {self.n} with {self.s} salary is working in {department} department')

# a=input('enter employee name: ')
# b=int(input('enter employee salary: '))
# c=input('enter department: ')
# emp=Manager(a,b)
# emp.dep(c)


"""2. Create a base class Shape with a method area(). Inherit it in Rectangle and implement the area method."""
# class Shape:
#     def area(self):
#         print('area of reactangle is width*height')
# class Rectangle(Shape):
#     def a():
#         pass
# x=Shape()
# x.area()



"""3. Design a class Person with attributes name and age. Create a class Student that adds grade.
 Display all attributes using an object of Student."""
# class Person:
#     def __init__(self, name,age):
#         self.n=name
#         self.a=age
# class Student(Person):
#     def accad(self, grade):
#         print(f'{self.a} year old {self.n} got {grade} grade in abaccus')

# a=input('enter student name: ')
# b=int(input('enter age: '))
# c=input('enter grade: ').upper()
# s=Student(a,b)
# s.accad(c)


"""4. Create a base class BankAccount and a derived class SavingsAccount with an interest calculation method."""
# class Bankaccount:
#     def __init__(self,balance):
#             self.b=balance
#             self.inter=((8/100)*balance)
# class Savingaccount(Bankaccount):
#     def interest(self):
#          print(f'the 8% annual interst on amount {self.b} is {self.inter}')

# a=int(input('enter the balance: '))
# p1=Savingaccount(a)
# p1.interest()


"""5 Create a class Vehicle and a derived class Car that overrides a method move()."""
# class Vehicle:
#     def move(self):
#         print('vehicle')
# class Car(Vehicle):
#     def move(self):
#         print('car')
#         super().move()
# x=Car()
# x.move()


"""6.Create a parent class Computer with method process().
Create a child class Laptop with method portable().
Show that the Laptop object can call both methods."""
# class Computer:
#     def process(self):
#         print('process')
# class Laptop(Computer):
#     def portable(self):
#         print('portable')

# x=Laptop()
# x.portable()
# x.process()


"""7.Create a parent class Vehicle with method fuel().
Create a child class Bike with method wheels().
Call both methods using the Bike object."""
# class Vehicle:
#     def fuel(self):
#         print('fuel')
# class Bike(Vehicle):
#     def wheels(self):
#         print('wheels')

# x=Bike()
# x.fuel()
# x.wheels()


"""8.Create a parent class Instrument with method play().
Create a child class Guitar with method strings().
Call both methods using the Guitar object."""
# class Instrument:
#     def play(self):
#         print('play')
# class Guitar(Instrument):
#     def strings(self):
#         print('guitar')

# x=Guitar()
# x.strings()
# x.play()


"""9.Create a parent class Parent with method say_hello().
Create a child class Son with method say_name().
Call both methods using the Son object.""" 
# class Parent:
#     def say_hello(self):
#         print('parent')
# class Son(Parent):
#     def say_name(self):
#         print('son')

# x=Son()
# x.say_hello()
# x.say_name()


"""10.Create a parent class Book with method pages().
Create a child class Novel with method story().
Call both methods using the Novel object."""
# class Book:
#     def pages(self):
#         print('book')
# class Novel(Book):
#     def story(self):
#         print('novel')

# x=Novel()
# x.pages()
# x.story()


"""11.Create a parent class Appliance with method power().
Create a child class Fan with method rotate().
Call both methods using the Fan object."""
# class Appliance:
#     def power(self):
#         print('fan is a appliance')
# class Fan(Appliance):
#     def rotate(self):
#         print('fan is a rotates')

# x=Fan()
# x.power()
# x.rotate()


"""12.Create a parent class Game with method start().
Create a child class Cricket with method score().
Call both methods using the Cricket object."""
# class Game:
#     def start(self):
#         print('seversl games')
# class Cricket(Game):
#     def score(self):
#         print('cricket is a game')

# x=Cricket()
# x.start()
# x.score()


"""13.Create a parent class College with method courses().
Create a child class Department with method faculty().
Call both methods using the Department object."""
# class College:
#     def courses(self):
#         print('college have courses')
# class Department(College):
#     def faculty(self):
#         print('department have faculty')

# x=Department()
# x.courses()
# x.faculty()


"""14.Create a parent class Teacher with method teach().
Create a child class ScienceTeacher with method lab().
Call both methods using the ScienceTeacher object."""
# class Teacher:
#     def teach(self):
#         print('teacher teaches')
# class Sceience_teacher(Teacher):
#     def lab(self):
#         print('science teacher have lab')

# x=Sceience_teacher()
# x.teach()
# x.lab()


"""15.Create a parent class Shape with method draw().
Create a child class Circle with method radius().
Call both methods using the Circle object."""
# class Shape():
#     def draw(self):
#         print('draw shape')
# class Circle(Shape):
#     def radius(self):
#         print('circle have radius')

# x=Circle()
# x.draw()
# x.radius()


"""16.Create a parent class Employee with method salary().
Create a child class Clerk with method duty().
Call both methods using the Clerk object."""
# class Employee():
#     def salary(self):
#         print('employee have salary')
# class Clerk(Employee):
#     def duty(self):
#         print('clerk have duty')

# x=Clerk()
# x.salary()
# x.duty()


"""17.Create a parent class Plant with method grow().
Create a child class Rose with method smell().
Call both methods using the Rose object."""
# class Plant():
#     def grow(self):
#         print('plants grow')
# class Rose(Plant):
#     def smell(self):
#         print('rose have good smell')

# x=Rose()
# x.grow()
# x.smell()


"""18.Create a parent class Device with method charge().
Create a child class Tablet with method touchscreen().
Call both methods using the Tablet object."""
# class Device():
#     def charge(self):
#         print('device need charge')
# class Tablet(Device):
#     def touchscreen(self):
#         print('tablet have touchscreen')

# x=Tablet()
# x.charge()
# x.touchscreen()


"""19.Create a parent class Bank with method services().
Create a child class ATM with method withdraw().
Call both methods using the ATM object."""
# class Bank():
#     def service(self):
#         print('bank services')
# class Atm(Bank):
#     def withdraw(self):
#         print('cash withdraw through atm')

# x=Atm()
# x.service()
# x.withdraw()


"""20.Create a parent class Sport with method play().
Create a child class Football with method goal().
Call both methods using the Football object."""
# class Sport():
#     def play(self):
#         print('playing sports')
# class Football(Sport):
#     def goal(self):
#         print('goal in football')

# x=Football()
# x.goal()
# x.play()


"""21.Create a parent class Language with method alphabet().
Create a child class English with method grammar().
Call both methods using the English object."""
# class Language():
#     def alphabet(self):
#         print('languages have alphabet')
# class English(Language):
#     def grammer(self):
#         print('english have grammer')

# x=English()
# x.alphabet()
# x.grammer()


"""22.Create a parent class Vehicle with method move().
Create a child class Bus with method passengers().
Call both methods using the Bus object."""
# class Vehicle():
#     def move(self):
#         print('vehicles moves')
# class Bus(Vehicle):
#     def passengers(self):
#         print('passengers in bus')

# x=Bus()
# x.move()
# x.passengers()


"""23.Create a parent class Building with method open().
Create a child class School with method students().
Call both methods using the School object."""
# class Building():
#     def open(self):
#         print('building have opening')
# class School(Building):
#     def students(self):
#         print('students go to school')

# x=School()
# x.open()
# x.students()

""".....................................multiple inheritance............................................."""

"""1.Create classes Person (name, age) and Employee (emp_id, department). 
Create a Manager class that inherits from both and display details."""
# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# class Employee:
#     def __init__(self,emp_id,department):
#         self.e=emp_id
#         self.d=department
# class Manager(Employee,Person):
#     def __init__(self,name,age,emp_id,department):
#         super().__init__(emp_id,department)
#         Person.__init__(self,name,age)
#     def pri(self):
#         print(f'{self.a} year old {self.n} is working in {self.d} having employee id-{self.e}')

# x=Manager('abhi',30,156,"devolepment")
# x.pri()


"""2.Create Student (name, roll), Marks (marks), and Result (inherits from both)."""
# class Student:
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
# class Mark:
#     def __init__(self,marks):
#         self.m=marks
# class Result(Mark,Student):
#     def __init__(self, marks,name,roll):
#         super().__init__(marks)
#         Student.__init__(self,name,roll)
#     def pri(self):
#         print(f'{self.n} with roll number {self.r} having {self.m} marks')

# x=Result(50,'abhi',1)
# x.pri()


"""3.Create two parent classes with the same method and see which one child calls."""
# class Student:
#     def meth(self):
#         print('student method')
# class Mark:
#     def meth(self):
#         print('mark method')
# class Result(Mark,Student):
#     def fun(self):
#         print('result method')
#         # super().meth()
#         Student.meth(self)

# x=Result()
# x.fun()


"""4.Create Vehicle (brand, model) and Features (color, fuel_type). Create Car that inherits from both."""
# class Vehicle:
#     def __init__(self,brand,model):
#         self.b=brand
#         self.m=model
# class Features:
#     def spec(self,color,fuel_type):
#         self.c=color
#         self.f=fuel_type
# class Car(Features,Vehicle):
#     def ca(self,name):
#         print(f'{self.b} {self.m} having {self.c} color in only {self.f} fuel only, its name is {name}')
#     def __init__(self,brand,model,color,fuel_type):
#         super().spec(color,fuel_type)
#         Vehicle.__init__(self,brand,model)


# x=Car('maruthi','alto','red','diesel')
# x.ca('zxi')


"""5.Create Addition and Multiplication classes and Calculator inherits from both."""
# class Addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         c=self.a+self.b
#         print(f'the sum of the first two numbers is {c}')
# class Multiplication:
#     def __init__(self,a,b):
#         self.f=a
#         self.g=b
#     def mul(self):
#         m=self.f*self.g
#         print(f'the multiplication result of the two last number is {m}')
# class Calculator(Addition,Multiplication):
#     def __init__(self, a, b,c,d):
#         super().__init__(a, b)
#         Multiplication.__init__(self,c,d)
#     def res(self):
#         super().add()
#         Multiplication.mul(self)

# a=int(input('enter first number: '))
# b=int(input('enter second number: '))
# c=int(input('enter third number: '))
# d=int(input('enter fourth number: '))
# x=Calculator(a,b,c,d)
# x.res()


"""6.Create Teacher (name, experience) and Subject (subject_name, code). Faculty inherits from both."""
# class Teacher:
#     def __init__(self,name,experience):
#         self.n=name
#         self.e=experience
# class Subject:
#     def __init__(self,sub_name,code):
#         self.s=sub_name
#         self.c=code
# class Faculty(Subject,Teacher):
#     def __init__(self, sub_name, code,name,experience):
#         super().__init__(sub_name, code)
#         Teacher.__init__(self,name,experience)
#     def pri(self):
#         print(f'you have {self.n} having {self.e} years of experice to teach {self.s}-{self.c}')

# x=Faculty('maths','03','anupama','4')
# x.pri()


"""7.Create Customer and Bank, then Account inherits from both."""
# class Customer:
#     def __init__(self,name):
#         self.n=name
# class Bank:
#     def __init__(self,bank):
#         self.b=bank
# class Account(Bank,Customer):
#     def __init__(self, bank,name):
#         super().__init__(bank)
#         Customer.__init__(self,name)
#     def pri(self):
#         print(f'mr. {self.n} having account in {self.b}')

# x=Account('canara bank','abhinand')
# x.pri()


"""8.Create Shape and Color, then Design inherits from both."""
# class Shape:
#     def __init__(self,shape):
#         self.s=shape
# class Color:
#     def __init__(self,color):
#         self.c=color
# class Design(Shape,Color):
#     def __init__(self, shape,color):
#         super().__init__(shape)
#         Color.__init__(self,color)
#     def pri(self):
#         print(f'{self.s} shape in {self.c} color')

# x=Design('round','green')
# x.pri()


"""9.Create Student and Sports, then champion inherits from both."""
# class Sports:
#     def __init__(self,item):
#         self.i=item
# class Student:
#     def __init__(self,student):
#         self.s=student
# class Champion(Sports,Student):
#     def __init__(self, item,student):
#         super().__init__(item)
#         Student.__init__(self,student)
#     def pri(self):
#         print(f'in {self.i} {self.s} is the new champion')

# x=Champion('long jump','arjun')
# x.pri()


"""10.Create Author and Publisher, then Book inherits from both."""
# class Publisher:
#     def __init__(self,name):
#         self.n=name
# class Author:
#     def __init__(self,auth):
#         self.a=auth
# class Book(Author,Publisher):
#     def __init__(self, name,auth):
#         super().__init__(auth)
#         Publisher.__init__(self,name)
#     def pri(self):
#         print(f'{self.n} publishes all the books by {self.a}')

# x=Book('DC','basheer')
# x.pri()


"""1.Create two parent classes:
•	Father with a method work() → print "Father goes to office".
•	Mother with a method cook() → print "Mother cooks food".
Then create a Child class that inherits from both and call both methods using an object of Child."""
# class Father:
#     def work(self):
#         print('Father goes to office')
# class Mother:
#     def cook(self):
#         print('Mother cooks food')
# class Child(Father,Mother):
#     def play(self):
#         print('child play')
#         super().work()
#         Mother.cook(self)

# x=Child()
# x.play()


"""2.	Create two parent classes:
o	Teacher with a method teach() → print "Teaching students".
o	Singer with a method sing() → print "Singing a song".
Then create a Student class that inherits from both and also has its own method study() → print "Studying hard".
Create a Student object and call all three methods."""
# class Teacher:
#     def Teach(self):
#         print('Teaching students')
# class Singer:
#     def sing(self):
#         print('Singing a song')
# class Student(Teacher,Singer):
#     def study(self):
#         print('Studying hard')
#         super().Teach()
#         Singer.sing(self)

# x=Student()
# x.study()


"""3.	Create two parent classes:
o	Dog with a method sound() → print "Dog barks".
o	Cat with a method sound() → print "Cat meows".
Then create a Pet class that inherits from both (Dog, Cat).
Create an object and call sound()."""
# class Dog:
#     def sound(self):
#         print('dog barks')
# class Cat:
#     def sound(self):
#         print('cat mews')
# class Pet(Dog,Cat):
#     def call(self):
#         super().sound()
#         Cat.sound(self)

# x=Pet()
# x.call()


"""4.	Create classes:
o	Father with method quality1() → print "Honest".
o	Mother with method quality2() → print "Caring".
o	Child inherits both and has method quality3() → print "Intelligent".
Show how the child inherits qualities from both parents."""
# class Father:
#     def quality1(self):
#         print('honest')
# class Mother:
#     def quality2(self):
#         print('caring')
# class Child(Father,Mother):
#     def quality3(self):
#         print('intelligent')
#         super().quality1()
#         Mother.quality2(self)

# x=Child()
# x.quality3()

"""...................................multilevel inheritance.............................................."""


"""Q1. Create classes: Bank → has method details() showing bank name.
Account (inherits Bank) → has method account_type(). Customer (inherits Account) → has method customer_info().
Write a program to show bank name, account type, and customer info."""
# class Bank:
#     def details(self,bank):
#         print('bank name: ',bank)
# class Account(Bank):
#     def account_type(self,type):
#         print('account type: ',type)
# class Customer(Account):
#     def customer_info(self,bank,type,cust):
#         print('varify your details................')
#         print('customer name: ',cust)
#         super().details(bank)
#         Account.account_type(self,type)

# bank=input('enter bank name: ')
# type=input('enter account type: ')
# cust=input('enter customer name: ')

# x=Customer()
# x.customer_info(bank,type,cust)


"""Q2. Class Vehicle → method info() shows “I am a vehicle”.
Class Car inherits Vehicle → method car_info() shows “I am a car”.
Class ElectricCar inherits Car → method battery_info() shows “I run on electricity”.
Create object of ElectricCar and call all methods."""
# class Vehicle:
#     def info(self):
#         print('i am a vehicle')
# class Car(Vehicle):
#     def car_info(self):
#         print('i am a car')
# class ElectricCar(Car):
#     def battery_info(self):
#         print('I run on electricity')
#         super().car_info()
#         Vehicle.info(self)

# x=ElectricCar()
# x.battery_info()


"""Q3. Class Person → stores name.
Class Student inherits Person → stores roll number.
Class Marks inherits Student → stores marks in 3 subjects.
Print student details with total marks."""
# class Person:
#     def name(self,name):
#         print('name: ',name)
# class Student(Person):
#     def roll(self,roll_no):
#         print('roll no: ',roll_no)
# class Marks(Student):
#     def mar(self,mark,roll_no,name):
#         print('marks in 3 subject: ',mark)
#         super().roll(roll_no)
#         Person.name(self,name)

# x=Marks()
# x.mar(78,1,'abhi')


"""Q4. Class Company → method company_info() prints company name.
Class Department inherits Company → method dept_info() prints department name.
Class Employee inherits Department → method emp_info() prints employee name and id.
Create employee object and display all details."""
# class Company:
#     def company_info(self,com_name):
#         print('company name:',com_name)
# class Department(Company):
#     def dept_info(self,dep_name):
#         print('department name: ',dep_name)
# class Employee(Department):
#     def emp_info(self,emp_name,dep_name,com_name):
#         print('employee name: ',emp_name)
#         super().dept_info(dep_name)
#         Company.company_info(self,com_name)

# x=Employee()
# x.emp_info('abhinand','web-development','congnito')


"""Q5. Write a program with 3 classes in a multilevel chain (A → B → C) where each has a constructor.
Use super() to show how constructors are executed one after another"""
# class A:
#     def __init__(self):
#         print('method a')
# class B(A):
#     def __init__(self):
#         print('method b')
#         super().__init__()
# class C(B):
#     def __init__(self):
#         print('method c')
#         super().__init__()

# x=C()


"""Q1. Online Shopping System (with Discount) Item → stores item name, price.
Cart (inherits Item) → stores quantity & calculates subtotal.
Customer (inherits Cart) → stores customer name and applies discount based on subtotal:
If subtotal > 5000 → 20% discount, If subtotal > 2000 → 10% discount, Else no discount
Final bill should be printed with all details."""
# class Item:
#     def __init__(self,name,price):
#         self.i=name
#         self.p=price
#     def name(self):
#         print(f'item name: {self.i}\nprice: {self.p}')
# class Cart(Item):
#     def __init__(self,quantity):
#         self.q=quantity
#     def car(self):
#         self.sub_total=self.q*self.p
#         print(f'quantity: {self.q}\nsub-total: {self.sub_total}')
# class Customer(Cart):
#     def __init__(self,cust_name,name,price,quantity):
#         self.n=cust_name
#         Item.__init__(self,name,price)
#         super().__init__(quantity)
#     def bill(self):
#         Item.name(self)
#         super().car()
#         if self.sub_total>5000:
#             discount=((20*self.sub_total)/100)
#             print('discount 20%: ',discount)
#         elif self.sub_total<5000 and self.sub_total>2000:
#             discount=((10*self.sub_total)/100)
#             print('discount 10%: ',discount)
#         else:
#             discount=0
#         print(f'total price: {self.sub_total-discount}\n\nThank You For Visiting Us Mr/Mrs {self.n}')

# n=input('enter item name: ')
# p=int(input('price: '))
# q=int(input('quantity: '))
# c=input('enter customer name: ')
# x=Customer(c,n,p,q)
# x.bill()



"""Q2. Vehicle Rental System Vehicle → stores vehicle name & base rent per day.
Car (inherits Vehicle) → stores car type (SUV, Sedan) and adds extra charges.
RentedCar (inherits Car) → stores rental days and calculates final rent.
Final bill should show vehicle, car type, base rent, extra charges, total rent."""
# class Vehicle:
#     def __init__(self,veh):
#         pass
#     def veh(self):
#         self.rentperday=2500
#         pass
# class Car(Vehicle):
#     def __init__(self,cartype,km):
#         pass
#     def car(self):

#         pass
# class Rented_car(Car):
#     def __init__(self,veh,cartype,km,day):
#         self.d=day
#         super().__init__(cartype,km)
#         Vehicle.__init__(self,veh)
#     def rented(self,rent_day,final_rent):
#         super().car()
#         Vehicle.veh()

    

# veh=input('vehicle name: ')    
# cartype=input('car type sedan/SUV: ') 
# km=int(input('enter total kilometer: '))
# day=int(input('rented days: '))
# x=Rented_car(veh,cartype,km,day)
# x.rented()



"""Q3. School Result Processing Person → stores student's name & roll number.
Exam (inherits Person) → stores marks in 5 subjects.
Result (inherits Exam) → calculates total, average, grade (A, B, C, Fail).
Use super() to chain constructors properly and display result."""

"""Q4. Bank Loan Processing
Bank → stores bank name. Account (inherits Bank) → stores account holder name & balance.
Loan (inherits Account) → stores loan amount, interest rate, duration.
Method to calculate EMI (Equated Monthly Installment). Print full loan details and EMI schedule."""

"""Q5. Multi-tier Company Payroll Company → stores company name.
Department (inherits Company) → stores department name.
Employee (inherits Department) → stores employee details (id, name, salary).
Payroll (inherits Employee) → calculates gross salary = salary + HRA (30%) + DA (20%) - Tax (10%).
Print complete payslip."""


