
    #FOR LOOP

#format of for loop
"""for var in iterable:
      block of loop"""       
    
# company='Quest'
# print(company)
# print(len(company))   #5 (len is a method used to find the length of an itterable)


#here looping means itterable the values
# company='Quest'
# for i in company:
#     print(i)

#range -when only one value it will be start from 0 and stop at that value
# for num in range(10):
#     print(num) 


# for num in range(1,20,2):     #-(start , stop ,step)                             #1 to 20 with 2 multiply
#     print(num)




#pass  -when we only put head of a statement not their footer its will be error of that free space(means for removing indentation error)

# for num in range(10):
#      pass    here no error bcoz of pass otherwise here indentation error will display


#break -is used to break means to stop the loop when that condition is true ( stop it where the is stated the condition)


# for i in range(10):
#     if i == 5 :        #here the condition is true thats why brak the value on the conditioned 5    (0,1,2,3,4)
#         break
#     print(i)


    #continue  -skip  of what we put on conditioned

# for i in range(20):
#     if  i == 15 :
#         continue
#     print(i)             #print 0 to 20 but the conditioned value 15 skip from there bcoz continue for skip the condition



# for char in "sreeraj":
#         if char in "AEIOUaeiou":   
#             continue
#         print(char, end="")         #s,r,r,j    (bcoz here skip the vowels in there of continue)

  #end="" -for the loops display in row wise side      



# for i in range(10):
#     print(i)
# else:
#     print("Execution Completed")      #here also display the else side message bcoz of direct print when here pass,break or continue condition its the else not work here  eg


    
# for i in range(10):
#     if i==8: 
#         break
#     print(i)             #here 0 to 7 out no look on the side of else bcoz here the break condition
# else:
#     print("Execution Completed") 


                #WHILE LOOP

#   		Statement(s)
# Example:i = 0
# 		while i < 5:
#     			print(i)
#     			i += 1

 
# i=1

# while i <=10 :
#     print(i)    # 1 to 10
#     i += 1

# else:
#     print("while completed")


    # Find the sum of numbers starting from 1 to 20 with for and while loop


    # for 
# total=0
# for i in range(1,21):
#     total += i

# print(total)

#while

# total=0
# i=1

# while i<=20:
#    total += i
#    i+= 1

# print(total) 



# print the odd number between 1 to 100 with for and while loop 
#for
# for i in range(1, 51, 2):
#     print(i)


#while
# i = 1

# while i <= 50:
#     print(i)
#     i += 2


    # value get from input and written between the even numbers with for and while
#for

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# if a%2 !=0:
#     a=a+1
# for a in range(a,b,2):
#     print(a)


#while


# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# if a%2 !=0:
#     a=a+1

# x=a
# while x<=b:
#     print(x)
#     x+=2


"""print the number 1-100 and skip the multiplies of 5"""

# for i in range(1,100):
#         if i%5==0:
#             continue
#         print(i)

"""find the multiplication table of 7  eg: 1x7=7"""

# for i in range(1,11):
#     print(f"{i}x7={i*7}")

"""find the factoial of number given by user"""

# using for loop

# n=int(input("Enter the number:"))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(fact)    #120  (5! = 5 × 4 × 3 × 2 × 1 = 120)


"""Find the given number by user prime or not"""

# number = int(input("Enter a number:"))


# for i in range(2,number):
#     if number % i == 0:
#         print("Not a prime")
#         break
# else:
#     print("prime")


"""Reverse a string     eg:  (name-abc = cba)"""


name ="shahil"

reverse=""

for i in name:
    reverse = i + reverse
print(reverse)      #lihahs


"""Reverse a integer number   eg:  (num-123 =321) """

num=1234

reverse=""

num=str(num)    

for i in num:
    reverse = i + reverse
print(reverse)     #4321