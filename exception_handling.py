
"""EXCEPTION HANDLING"""

# Exception handling is pyhton used to handle runtime errors,so that the normal flow of the program maintained.without it,
# your programn will crash if an error occurs

""" 3 ERRORS """
 # Syntax Error
 # Runtime Error
 # Logical Error


"""sytntax of exception handling"""

# try:
    #code that may raise an exception          

# except exception type:
    #code to handle the exception             #(except work when there is error , otherwise if no error else will work)

# else:
    #excecutes if no exception occurs         #(else only work when there is no error ,only when cose is correct)

# finally:
    #always executes,even if there is an exception       #(here finally work for message its work when code is error or not error)


"""EG:"""

# print("division of two numbers")
# x=int(input("enter first number : "))
# y=int(input("enter second number : "))

# try:
#     z=x/y                                      #code to try

# except ZeroDivisionError:
#     print("second value doesnt be zero")            #handling when error

# else:
#     print(z)                            #else when not error

# finally:
#     print("++++++++++++++++")              #always print





"""     RAISE - (user defined exception)     """

# Raise is used to raise an exception with condition (its most likely with if)
# Raise keyword used to manually create(throw) an exception
#if you want to raise(generate) an error yourself , python provise the raise keyword  (used to someone who want to create own exception when a condtition is wrong)

#raise exception passes to except by means to handle after raise ,used by   (except Exception as a "variable name")



"""simple eg of raising:"""

# x=10
# x="abc"

# if not type(x) ==int:
#     raise Exception("only numbers are allowed")

# else:
#     print(x)


#----------------------------------------------------------------------------------------------------------
""" here handle the raised exception eg:"""
#----------------------------------------------------------------------------------------------------------


# try:
#     x="shahil"
#     # x=1500

#     if type(x) !=int:
#         raise Exception("only numbers are allowed $$$$$")
    
# except Exception as k:                          #here k is variable = store the value of raise into the k
#     print("Exception occured:",k) 

# else:
#     print(x)

# print("hello friends")            #its only to know no problem oke all are



#----------------------------------------------------------------------------------------------------------
"""exception handling of raise in using function"""
#----------------------------------------------------------------------------------------------------------

def division(x,y):
    if y==0:
        raise ZeroDivisionError("divisor can't be zero")
    else:
        return x/y
    
try:
    # print(division(10,2))
    print(division(20,0))

except ZeroDivisionError as a:
    print("error occured:",a)

print("+++++++++++++++++++++")                          #just to know nothing happen to normal flow



#----------------------------------------------------------------------------------------------------------
""" user defined exception class """
#----------------------------------------------------------------------------------------------------------


class Myerror(Exception):
    pass

try:
    x=500
    if x<10:
        raise Myerror("value is too small")
    
except Myerror as a:
    print("An exception occured",a)

else:
    print("too small")

print("welcome")