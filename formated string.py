            #SECTION A

#1. Create two variables: name and age. Print them using comma method.
  # Name: Anu Age: 21
  
name = "shahil"
age =19

print("Name:",name ,"Age:",age)


#2. Create variables city and country. Print them in one line using comma.

city = "manjeri"
country = "india"

print(city , country)


#3. Create three integer variables a, b, c. Print their values using comma.

a=10
b=20
c=30

print(a ,b ,c)


# 4. Print the message:
#    Hello Python Students
#    using two variables and comma.

a= "Hello Python"
b= "Students"
print(a , b)

#5. Store your college name and course name in variables and print using comma.

college = "QIS ACADEMY"
course ="python"

print("College Name:" ,college , "Course Name:" , course)


                #SECTION B



# 6. Create a variable name and print:
#    My name is <name>
#    using + operator.

a="My Name is "
b="Shahil"
print(a+b)


# 7. Create variable age and print:
#    I am <age> years old
#    using + operator. (Use str())

age="19"
print("I am "+ age +" years old")


# 8. Create variables a=10 and b=20.
#    Print:
#    The sum is 30
#    using + operator.

a=10
b=20
print("The sum is "+str(a+b))


# 9. Create variable country and print:
#    I live in <country>
#    using + operator.

country="india"

print("I live in "+country)


# 10. Try printing string + integer without str() and note the error.

# a=10
# b=20
# c=a+b
# print("The sum is " + c) #error


# 11. Create variables name and age.
#     Print them using f-string.

name="shahil"
age=19

print(f"{name} {age}")


# 12. Create variables a=5 and b=10.
#     Print:
#     Sum of 5 and 10 is 15
#     using f-string.

a=5
b=10

print(f"sum of {a} and {b} is {a+b}")



# 13. Create variable price=50 and qty=3.
#     Print total amount using f-string.

price=50
qty=3
print(f"{price*qty}")

# 14. Create variable name and print it in uppercase using f-string.  -(not studied)

name="shahil"
print(f"{name.upper()}")


# 15. Create variable x=7 and print its square using f-string.

x=7
print(f"{x**2}")




# 16. Print the same output using:
#     a) comma
#     b) + operator
#     c) f-string

  #   Output:
  #  My age is 25

  # a)
age=25
print("My age is",age)
print("My age is "+str(age))
print(f"My age is {age}")



# 17. Print:
#     Welcome <name> to Python class
#     using all three methods.

name="Shahil"
print("Welcome",name,"to Python class")
print("Welcome "+name+" to Python class")
print(f"Welcome {name} to Python class")


# ========================================
# SECTION E – REAL WORLD BASED QUESTIONS
# ========================================

# 18. Create variables: product, price.
#     Print:
#     Product: Laptop Price: 45000
#     using f-string.

product="Mac pro" 
price=45000
print(f"product:{product} Price:{price} ")


# 19. Create variables: employee_name, salary.
#     Print:
#     Employee Anu earns 30000 per month
#     using f-string.

employee_name="Anu"
salary=30000
print(f"Employee {employee_name} earns {salary} per month")

# 20. Create variables: movie_name, rating.
#     Print:
#     Movie Avatar has rating 4.5
#     using comma and f-string.

movie_name="Avatar"
rating=4.5
print("Movie",movie_name,"has rating",rating)
print(f"Movie {movie_name} has rating {rating}")


# SECTION F – CHALLENGE QUESTIONS
# ========================================

# 21. Create 3 subject marks and print total and average using f-string.
maths=80
chemistry=60
physics=40
print(f"{maths+chemistry+physics}")
print(f"{(maths+chemistry+physics)/3}")


# 22. Create variable name and print:
#     Hello <name>, Welcome to Quest!
#     using f-string.

name="Shahil"
print(f"Hello {name}, Welcome to Quest!")

# 23. Create variables length and breadth.
#     Print area of rectangle using f-string.

# length=50
# breadth=5
# print(f"{length*breadth}")

# 24. Ask user input for name and age, then print using f-string.
# a=input("Enter Your Name:")
# b=input('Enter your age:')
# print(f" {a} {b} ")

# 25. Create a bill format using f-string:
#     Item: Pen
#     Price: 10
#     Quantity: 5
#     Total: 50

item="pencil"
price=20
Quantity=5
Total= price*Quantity
print(f"item:{item}\n price:{price}\n Quantity:{Quantity}\n  Total:{Total}")



# ========================================
# SECTION G – MINI ASSIGNMENT
# ========================================

# Assignment 1:
# Create a simple Student Profile program.
# It should print:
# - Name
# - Age
# - Course
# - College
# Using f-strings.

name="Neha"
age=19
course="BCA"
college="Noble manjeri"
print(f"Name:{name}\n Age:{age}\n Course:{course}\n College:{college}")

# Assignment 2:
# Create a Shopping Bill program.
# Take input:
# - Item name
# - Price
# - Quantity
# Print formatted bill using f-string.

a=input("Item name:")
b=int(input("Price:"))
c=int(input("Quantity:"))
print(f"item:{a}\n price:{b}\n quantity:{c}\n Total price:{b*c}")

# Assignment 3:
# Create an Employee Salary Slip program.
# Print:
# - Employee_Name
# - Basic Salary
# - HRA
# - DA
# - Total Salary
# Using f-string.

a=input("Emplyee Name")
b=input("Basic salary")
c=input("HRA")
d=input("DA")
Total =int(b+c+d)
print(f'{a}\n {b}\n {c}\n {d} ')