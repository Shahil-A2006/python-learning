"""HERE USER DEFINED MODULE"""
"""above three file sare the build in functions here i do the user define module by importing the next py files"""
"""I would do the operatiopns here the file my module and i call this at the next file name MyModule Result by importing there"""
"""Here module used by import next file by import -file name       & we can access the code what we want by call the filename and what we want to acces"""


# def add(a,b):
#     return a+b


# def diff(a,b):
#     return a-b

# def mul(a,b):
#     return a*b



# ------------------------------------------------------------------------------------------------------------

"""Root pf a quadratic equation ax^2 + bx + c = 0"""
"""square root finding with user module"""

def quadratic_root(a,b,c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No Real Roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root{root}"
    else:
        root1= (-b + math.sqrt(discriminant)) / 2*a
        root2= (-b - math.sqrt(discriminant)) / 2*a
        return f"The Real Roots are {root1,root2}"
    

# here the same of above but silly diff from above at doing methods

import math
def quad_root(a,b,c):
    x=math.sqrt(b**2-(4*a*c))
    if x<0:
        print('there is no real root available')
    elif x==0:
        print(-b/(2*a))
    else:
        print(f"root 1: {(-b+x)/2*a}")
        print(f"root 2: {(-b-x)/2*a}")