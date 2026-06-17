"""2.  Positive, Negative or Zero Write a program to check if a number is positive, negative or zero."""
# num=int(input("enter the number: "))
# if num>0:
#     print("Positive number")
# elif num<0:
#     print("Negative number")
# else:
#     print("Zero")

"""3.  Find the Largest of Two Numbers Take two numbers from the user and print the larger one."""
# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# if num1>num2:
#     print("Larger one is: ",num1)
# elif num1<num2:
#     print("Larger one is: ",num2)

"""4.  Find the Largest of Three Numbers Take three numbers and print the largest among them."""
# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# num3=int(input("enter third number: "))
# if num1>num2 and num1>num3:
#     print("Larger one is: ",num1)
# elif num2> num1 and num2>num3:
#     print("Larger one is: ",num2)
# else:
#     print("Larger one is: ",num3)

"""6.  Pass or Fail Ask the user for their mark and print Pass if mark is 40 or above, otherwise Fail."""
# mark=int(input("enter your mark: "))
# if mark>100:
#     print("not a valid number")
# elif mark>=40:
#     print("Pass")
# else:
#     print("Fail")

"""8.  Leap Year Checker Input a year and check whether it is a leap year or not."""
# year=int(input("enter year: "))
# a=4
# if year%4==0:
#     print("leap year")
# else:
#     print("not leap year")

"""9.  Divisible by 5 and 11 Check whether a number is divisible by both 5 and 11."""
# num=int(input("enter number: "))
# if num%5==0 and num%11==0:
#     print("divisible by 5 and 11")
# else:
#     print("not divisible")

"""10. Check Character Type. Input a character and check if it is a vowel or consonant."""
# chara=str(input("enter a alphabet: "))
# if chara in ["a","e","i","o","u"]:
#     print("character is vowel")
# else:
#     print("not vowel")

"""12. Number Comparison Game Take two numbers. If first is greater print “First is greater”, else print “Second is greater”."""
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# if a>b:
#     print("first number is greater")
# else:
#     print("second number is greater")

"""13. Check Temperature If temperature > 30 print Hot, if between 20 and 30 print Warm, else Cold."""
# temp=int(input("temperature: "))
# if temp>30:
#     print("Hot")
# elif 20<=temp<=30:
#     print("Warm")
# else:
#     print("Cold")

"""14. Check Salary Bonus If salary > 50000, give bonus 5000 else bonus 2000. Print total salary."""
# salary=int(input("enter your salary: "))
# if salary>=50000:
#     print(f"you have 5000 as bonus \ntotal salary is {salary+5000}")
# else:
#     print(f"you have 2000 as bonus \ntotal salary is {salary+2000}")

"""15. Check Shopping Discount If bill amount > 1000, give 10% discount else no discount."""
# bill=int(input("enter the bill amount: "))
# if bill>=1000:
#     print(f"hooray you are eligible for 10% discount\ntotal amount is: {bill-(bill*0.1)}")
# else:
#     print(f"total amount is: {bill}")

"""16. Age Category If age < 13 print Child If age between 13 and 19 print Teen Else print Adult"""
# age=int(input("enter your age: "))
# if age<13:
#     print("Child")
# elif 13<=age<=19:
#     print("Teen")
# else:
#     print("Adult")

"""17. Electricity Bill Calculator (Simple) If units <= 100 charge 2 per unit If 101-200 charge 3 per unit Above 200 charge 5 per unit"""
# unit=int(input("enter the consumed unit: "))
# if unit<=100:
#     print(f"unit charge is 2 Rupees.\ntotal bill amount: {unit*2}")
# elif 101<=unit<=200:
#     print(f"unit charge is 3 Rupees.\ntotal bill amount: {unit*3}")
# else:
#     print(f"unit charge is 5 Rupees.\ntotal bill amount: {unit*5}")

"""18. Check Number is Multiple of 3 or 7 Input a number and check if it is multiple of 3 or 7."""
# num=int(input("enter number: "))
# if num%3==0 or num%7==0:
#     print("it is multiple of 3 or 7")
# else:
#     print("not a multiple of 3 or 7")

"""19. Check Password Strength If password length >= 8 print Strong Password else Weak Password."""
# password=input("enter your password: ")
# if len(password)>=8:
#     print("strong password")
# else:
#     print("weak password")

"""20. Find Smallest of Two Numbers Take two numbers and print the smaller one."""
# num1=int(input("enter first no: "))
# num2=int(input("enter second no: "))
# if num1>num2:
#     print("the smaller no is: ",num2)
# else:
#     print("the smaller no is: ",num1)