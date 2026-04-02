#operators

# num1=10
# num2=15

# text1="ab"
# text2="cd"

"""arithemetic operators"""

# print(num1+num2) #25

# print(text1+text2) #abcd (string concatination)

# ##################################

# print(num1*num2) #150

# print(num1*text1)   #abababababababababab    (repetition operation)
# # print(text1*text2)  #error

# ##################################

# # %(for reminder)
# a=30
# b=7
# print(a%b)   #2

# #**(exponental)
# a=10
# print(a**2) #100

# # //floor division(how many in there)
# n=20
# m=4

# print(n // m) #5 (there how many times 4 in 20)


"""comparison operator"""

# num1=10
# num2=20

# str1="abc"
# str2="abc"
# # == (equal to)
# print(num1 == num2)  #false
# print(str1 == str2)  #True

# #!= (not equal to)
# num1=10
# num2=10
# print(num1 != num2) #false

# num1=15
# num2=10
# print(num1 > num2) #true

# print(num1 < num2)  #false

# num1=10
# num2=10
# print(num1 >= num2) #true

# num1=4
# num2=10
# print(num1 <= num2)  #true



"""Assignment operators"""

# a=10
# b=20
# a+=b  #a= a+b
# print(a)  #30


"""Membership operator""" #use to it is there to check


# #in       is there its true otherwise false

# sentence="My domain is python"

# print("is" in sentence)

# #not in      is there is false opp to the in

# sentence="I am shahil"

# print("am" not in sentence)




"""Identity Operators"""

# #is  - it is check only id means memory location same the id also same other two different valye id also different
# num1=10
# num2=10

# print(id(num1)) #140717842425032
# print(id(num2)) #140717842425032


# print(num1 == num2) #true
# print(num1 is num2) #true    

# #diff value
# num1=10
# num2=20

# print(id(num1)) #140717842425032
# print(id(num2)) #140717842425032


# print(num1 == num2) #false
# print(num1 is num2) #false


# #is not -diff of is check that diff memory location

# num1=[10,20,30]
# num2=[10,20,30]

# print(num1 == num2)  #true
# print(num1 is not num2) #true


"""Logical operator"""

#and - True if both conditions are true

num1 = 10
num2 = 5

print(num2 < num1 and num2>3) #True bcoz both are true condition


#or - True if at least one condition is true

num1 = 10
num2 = 5

print(num2 < num1 or num2>6) #True here first condition only true but its out will true bcoz its Or

#not - Reserves the result means answer is opposite of what the condition

num1 = 10
num2 = 5

print(not (num2 < num1))  #False bcoz its not here happens just oppossite of condition
