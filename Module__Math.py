"""MODULE"""

# collection of .py files is called module
# "import" is used to connect with two files.
# two types- built-in and user defined
# collection of modules is called as "package"
# for sin, cos, tan should give radian values to execute	[print(math.sin(math.radians(90)))]
# python inbuilt power module return a integer value where as the math.pow() return a float value.


"""MATH"""


import math                 #to connect as math we doing math

# print(math.pi)       #pi value
# print(math.e)          #
# print(math.sqrt(25))    #square root
# print(math.pow(2,2))    #power (to square ,cube ......)                 
# print(math.fabs(-10)) #10.0 #floating absolute value ,to remive sign and answer as float
# print(math.ceil(4.2))   #5  #to round at highest value bcoz its ceil 
# print(math.floor(4.9))  #4    #get lowest value with remove float bcoz floor
# print(math.gcd(12,18))  #6   #highest common divisor
# print(math.sin(90)) #0.8939966636005579    #to get sin but here not get proper value to get proper use radian eg belows  
# print(math.cos(90))
# print(math.tan(90)) 
# print(math.sin(math.radians(90)))  #1.0    -here radians for the proper value     (radian is also for calculate another like term of angle but here math can accept radian)
# print(math.cos(math.radians(0)))   #1.0
# print(math.tan(math.radians(45)))    #0.9999999999999999
# print(math.radians(180))
print(pow(2,2))  #also get power with removing floating value