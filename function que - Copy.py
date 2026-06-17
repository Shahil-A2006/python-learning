"""1.create multiplication table with function , number given by zero"""

# def mul(num):

#     for i in range(1,10):
#         print(n,"x",i ,"=",n*i)

# n=int(input("enter a number: "))
# mul(n)


"""2.check whether a number is posivie,negative or zero"""

# def check():
#     a=int(input("enter a number:"))
#     if a>0:
#         print("Its a positive number")
#     elif a<0:
#         print(" Its a negative number")
#     else :
#         print("Its zero")
    
# check()


"""3.check whether a number is odd or even"""

# def check():
#     x=int(input("enter a number: "))

#     if x==0:
#         print("zero")
#     elif x % 2 ==0:
#         print("its even number")
#     else:
#         print("its odd number")
    
# check()


"""4.find sum and average of list of numbers"""

# lst=[]
# limit=int(input("enter the limit: "))

# for i in range(limit):
#     num=int(input(f"enter the {i+1} value of list: "))
#     lst.append(num)

# print(lst)

# def calculate(num):
#     total = 0

#     for i in num:
#         total = total + i
#     print(f"Sum {total}" )

#     average=total/len(num)
#     print(f"Average {average}")

# calculate(lst)
    

"""5.find rev of numbers"""

# Function to reverse a number

# def reverse_number(num):
#     rev = 0

#     while num != 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     print("Reversed Number =", rev)



# n = int(input("Enter a number: "))


# reverse_number(n)  

"""6.find the sum of digits of numbers"""

# def sum_digits(n):
#     s = 0

#     for i in str(n):
#         s = s + int(i)

#     return s


# num = int(input("Enter a number: "))
# print("Sum of digits:", sum_digits(num))

"""7.find rev of string"""

# def rev():
#     a=input("enter a string: ")
#     b=""

#     for i in a:
#         b=i+b

#     print(b)
# rev()


"""8.pallindrome check number"""

# def palindrome():
#     num = int(input("Enter a number: "))
#     temp = num
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     if temp == rev:
#         print("Palindrome Number")
#     else:
#         print("Not a Palindrome Number")

# palindrome()


"""9.pallindrome check string"""

# def palindrome():
#     text=input("Enter a string: ")
#     rev=""

#     for i in text:
#         rev=i+rev

#     if text == rev:
#             print("Palindrome String")
#     else:
#          print("Not a Palindrome string")

# palindrome()




"""10.factorial of number"""

# def factorial():
#     num = int(input("Enter a number: "))
#     fact = 1

#     for i in range(num, 0, -1):
#         fact = fact * i

#     print("Factorial =", fact)

# factorial()

"""11.Amstrong check"""

# def armstrong():
#     num = int(input("Enter a number: "))
#     temp = num
#     total = 0

#     while num > 0:
#         digit = num % 10
#         total = total + (digit ** 3)
#         num = num // 10

#     if temp == total:
#         print("Armstrong Number")
#     else:
#         print("Not an Armstrong Number")

# armstrong()

"""12.Maximum of two numbers"""

# def maximum():
#     a=int(input("Enter First Number: "))
#     b=int(input("Enter Second Number: "))

#     if a>b:
#         print("Maximum Number: ",a)
#     else:
#         print("Maximum Number: ",b)

# maximum()

    

"""13.Prime Number Check in functions"""

# def prime():
#     num = int(input("Enter a number: "))

#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print("Not a Prime Number")
#                 break
#         else:
#             print("Prime Number")
#     else:
#         print("Not a Prime Number")

# prime()

"""14.Count vowels in a string"""

# def vowels():
#     text=input("enter a text: ")
#     count=0

#     for i in text:
#         if i in "aeiouAEIOU":
#             count = count + 1

#     print("Number of Vowels = ",count)

# vowels()


"""just to understand dont imp to mind its for just variable declaree to understand"""
# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(3)

  
"""  *args(arbitary arguments) & **kargs(keyword arbitrary varibale) """

"""14. add multiple numbers"""

# def add():
#     a=[]
#     for i in range(x):
#         y=int(input("enter numbers: "))
#         a.append(y)
#     sum=0
#     for i in a:
#         sum+=i
#     print(f"the sum of the numbers is : {sum}")
# x=int(input('enter limit: '))
# add()

"""15. multiply multiple numbers"""

# def multiply():
#     limit = int(input("How many numbers: "))
#     result = 1

#     for i in range(limit):
#         num = int(input("Enter number: "))
#         result = result * num

#     print("Multiplication =", result)

# multiply()

"""16. find maximum number"""
"""17. count total arguments"""
"""18. find average of numbers"""
"""19. student details (name, age, course, grade)using **(keyword arguments)
    1. display variable
    2. display keys
    3. display values
    4. display key value pairs"""
"""20. user login details (username, password, role) using **"""


#RECURSION QUESTIONS

"""1.Factorial of a number"""

# def factorial(n):
#     if n ==1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(10))
    


"""2.Fibonacci Series"""

"""3.Add Numbers from 1 to n"""

# def sum(n):
#     if n == 1:
#         return 1
#     else:                      
#        return n + sum(n-1)
    
# num=int(input("Enter a Number: "))
                                                                                                                                                                                      
# print(sum(num))
    
"""4.Power of a number"""

"""5.Sum of Numbers"""

# def add(n):
#     if n == 1:
#         return 1
#     else:
#         return n + add(n - 1)

# num = int(input("Enter a number: "))
# print("Sum =", add(num))




"""QUE OF ANNONIMUS FUNCTION / LAMBDA FUNCTION"""

"""1. Square of a Number """

# square=lambda a:a**2
# print(square(5))

"""2. Add Two Numbers   """

# add=lambda x,y : x+y
# print(add(50,50))

"""3. Cube of a Number """

# square=lambda a:a**3
# print(square(5))

"""4. Find Maximum of two Numbers """

# max_num = lambda a, b: a if a > b else b if b > a else "equal"
# print(max_num(10, 20))

"""5. Check Even or Odd """

# num=int(input("enter a number: "))
# check=lambda n: "even" if n %2 ==0 else "odd"
# print(check(num))


"""QUE OF MAP FUNCTION """

"""1.  Find Squares of List Elements """

# lst= [2,4,6,8,10]
# square=list(map(lambda n:n**2,lst))
# print(square)

"""2.  Convert Names to Uppercase """

# names=["shahil",100,"shanoon","fathimabeevi",500,"ashraf"]
# upper=list(map(lambda a: a.upper() if type(a) == str else "",names))
# print(upper)

""" 3. Add Two Lists Using Map  """

# lst1=[10,20,30]
# lst2=[40,50,60]

# add=list(map(lambda x,y : x+y ,lst1,lst2))
# print(add)

"""4.  Find Length of Each String in a List """

# str=["shahil","shanoon","fathimabeevi","ashraf"]
# length=list(map(lambda x: len(x) , str))
# print(length)


""" 5.  Convert Celsius to Fahrenheit """

# celsius=[0,10,20,30,40,50]
# fahrenheit=list(map(lambda x: (x *9/5) +32,celsius))
# print(fahrenheit)




# ===================
"""       QUE OF FILTER FUNCTION """
# ===================
""" 1.  Find Even Numbers in a List  """

# lst=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x: x%2 ==0 ,lst))
# print(even)

""" 2.  Find Odd Numbers in a List  """

# lst=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x: x%2 !=0 ,lst))
# print(even)

"""3.  Filter Names Starting with 'A'  """

# names=["shahil","ashraf","shanoon","aman"]
# starts=list(filter(lambda x: x.startswith("a"),names))
# print(starts)

""" 4.  Filter Words Longer than 5 Characters """
#  Filter Positive Numbers from a List
#  Filter Numbers Greater than 50

# combined questions
# =======================
#  Find Squares of Even Numbers in a List
#  Convert Names Starting with 'A' to Uppercase
#  Add Two Lists and Filter Even Results




# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# result = list(map(lambda x, y: x + y, list1, list2))

# print(result)