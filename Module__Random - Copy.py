"""MODULE"""



""" RANDOM"""
"""This is buid in module"""


import random                   ##to connect as random we doing random values

# n=random.random()
# print(n)                                #randomly generate num between 0 to 1  , 0and 1 not include

# ---------------------------------------------------------------------------------------------- 
# n=random.randint(2,10)
# print(n)                                #randomly num generate from 2 to 10  , 2 and 10 included

# ----------------------------------------------------------------------------------------------
# n=random.randint(100,999)               #randomly num generate from 100 to 999
# print(n)                                #3 digit
# ----------------------------------------------------------------------------------------------

"""OTP GENERATION"""
# for i in range(6):                          #for loop 6 digit generate
#     print(random.randint(0,9),end="")       #diff 6 digit values

# ----------------------------------------------------------------------------------------------

# n=random.randrange(10,200,2)            #to generate even numbers randomly ,10 include , 200 not include
# print(n)                                   #starting value will decide it odd or even , here starting value is even thats why its even

# ----------------------------------------------------------------------------------------------

# n=random.randrange(11,200,2)            #to generate odd numbers randomly ,11 include , 200 not include
# print(n)                                  #starting value will decide it odd or even , here starting value is odd thats why its even

# ----------------------------------------------------------------------------------------------

# lst=[10,30,"shahil",True,"hey",500,250,"hello"]
# random.shuffle(lst)
# print(lst)                               #to shuffling the list


# ----------------------------------------------------------------------------------------------

lst1=[10,30,"shahil",True,"hey",500,250,"hello"]
m=random.choice(lst1)
print(m)                  #to randomly select an element from a list

# ----------------------------------------------------------------------------------------------
