#FUNCTION

"""function is a block of code which only runs when its called"""
"""function only do with the keyword def , otherwise its not function"""
"""speciality of function is we can reuse it how much we want by calling the function name only."""
"""instruction must be code after the indentaqtion ,indentation is must"""

#syntax model

# def welcome():                        #function name welcome()
#     print("Hi Hello Welcome")         #content of function ? body of function

# welcome()                             #calling the name for output


# def welcome():
#     print("Hello Shahil")
# welcome()



# def welcome():
#     name="shahil"
#     print("Hello ",name)
# welcome()


# def welcome(name):     #parametre -put variable here at parameter        -parameter also called formal parameter
#     print("Hello ",name)

# welcome("Shahil")     #argument -put value of the parameter varible here at argument      -argument also called actual parameter



""""""
# def hello():
#     x=input("enter name:")
#     print("hi",x)
#     x=input("how is your day:")
#     print("great to hear that your day is",x)
# hello()


"""Return keyword -"""  """used to return the out of the space print ,here call the function after return call on the print otherwise it's don't work   eg: """

# def welcome():
#     return "Hello Shahil"
# print(welcome())     #Hello Shahil



"""Object Calling -""" """it is just ccalling function name place it assign into variable and call with that variable """

# def welcome():
#     return "Hello Shahil"
# ob=welcome()
# print(ob)    #Hello Shahil


"""Pass  - in function if we do def andd fn name and not code body of that it will be error ,we can solve this problem by using pass"""
"""pass used to simply for while no body in a function it will error , when put pass there we solved it"""

def welcome():
    pass                  ##to ignore the function with no error in the code


"""call in return with use of a variable"""

# def welcome():
#     name="shahil"
#     return f"Hello {name}"
# print(welcome())    #Hello shahil
              

 
"""Parameter and Argument   - at the place of define fn ( its parameter) - at the place of calling fn(its argument)"""

# def welcome(name):
#     print("Hello",name)
# welcome("guysss")
# welcome("friendssss")


# def num(a):
#     print("enter the number here:",a)
# num(5)                                     #enter the number here: 5


# def num(a):
#     print("enter the number here:",a)
# b = 5
# num(b)                #enter the number here: 5    - argument is pass there b but going the variable b value


""" parameter and argument with return keyword """

# def welcome(name):
#     return f"hello {name}"
# print(welcome("guyssssssss"))
                                    

""" MULTIPLE ARG & PARA -""" """we can put multi no.of values how much we want para & arg but we assure that the parameter and argument has same no.of values wanted    eg:"""
"""if there is two parameter must have three on argument   otherwise error"""

# def add(a,b):
#     print(a+b)
# add(10,10)         #20 - with normal print


# def add(a,b):
#     return a+b
# print(add(10,10))   #20 - with return keyword


# def person(name,place):
#     print(f"my name is {name}")
#     print(f"my place is {place}")
# person("shahil","malappuram")



"""DEFAULT ARGUMENT -""" """(Set argument defaultly on the parameter)its thats assign the value of argument defaultly at the place of patrameter - thats why there take from there andd no error happen A"""

# def person(name,place= "malappuram"):
#     print(f"my name is {name}")
#     print(f"my place is {place}")
# person("shahil")


"""KEYWORD ARGUMENT-""" """here the varibale assinged at para called only in arg and assing it , if it any ways not order of values put like blow eg not problem take as print"""

# def person(name,place):
#     print(f"my name is {name}")
#     print(f"my place is {place}")
# person(place="malappuram",name="shahil")


"""Mixing Position Keyword Argument -"""  """means only we put first only positioned and aftyer only keyword there opp to this its error"""


# def person(name,place):
#     print(f"my name is {name}")
#     print(f"my place is {place}")
# person("shahil",place="manjeri")    #correct - bcoz fist we put only position all position put first after keywoed can set  after that only keyword put
# print(place="manjeri","shahil")        #error -bcoz here first key put its error not put first key word only position put at first otherwisw error



"""iterating the diff types in function"""
"""eg: here list iterating in the fn and print by calling"""

# def demo(a):
#     for i in a:
#         print(i)

# lst=[10,20,30,"shahil"]
# demo(lst)     #here iterate the list using fn


"""here call with index in return list or any type but only get  any object can define ther eg:"""

# def demo():
#     return ["red","green","blue","black"]
# a=demo()
# print(a[0])   #red
# print(a[2])   #blue


"""here call with variable and assign the value as order to the variable order eg:"""

# def demo():
#     return ["red","green","blue","black"]

# a,b,c,d = demo()
# print(a) #red
# print(c) #blue


# def calc(a,b):
#     return a+b,a-b

# print(calc(10,6))   #(16, 4)

# a,b=calc(10,10)
# print(a)     #20
# print(b)     #0


"""here argument assign with the variable ,store number on variable in the fn """

# def calc(a,b):
#     return a+b

# a=50
# b=50
# print(calc(a,b))   #100   - here i code variable name in argument here take the value in the argument


"""here i same with take input from use in the variable and that variable store in argument"""

# def cal(a,b):
#     return a+b

# a=int(input("enter a  umber: "))
# b=int(input("enter another number: "))            #here before input i define integer by int bcoz there is + operator in the return
# print(cal(a,b))



"""here do with add,sub,mult,div """

# def add(a,b):
#     return f"sum: {a+b}"

# def sub(a,b):
#     return f"difference: {a-b}"

# def mul(a,b):
#     return f"product: {a*b}"

# def div(a,b):
#     if b!=0:
#         return f"division: {a/b}"
#     else:
#         return "divisor not be zero"
    

# a=int(input("enter a number: "))
# b=int(input("enter another number: "))

# print(add(a,b))
# print(sub(a,b))
# print(mul(a,b))
# print(div(a,b))



"""calculations"""

# def ad(a,b,c):
    
#     if b=='+':
#         return f'addition result {a+c}'
#     if b=='-':
#         return f'substraction result {a-c}'
#     if b=='*':
#         return f'multiplication result {a*c}'
#     if b=='/':
#         return f'division result {a/c}'
#     else:
#         pass
# a=int(input('enter first number: '))
# b=input('enter opeartion: ')
# c=int(input('enter second number: '))   
# print(ad(a,b,c))




"""

arbitrary variable (* before the variable)
keyword arbitrary varibale (** before the variable)
                                                        """



"""RECURSIVE FUNCTION"""

# A recursive function is a function that calls itself to solve a problem.

#Every recursive function has 2 main parts
#     1.base case:
# condition where the function stop calling itself
#       2.Recursive case:
#   the function calls itself witha smaller/simpler input  

#eg:

#factorial of a number

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))





"""ANNONIMUS FUNCTION"""

#  An Annonimus function is a function without a name 
        
#  In python ,we create annonymous function using the keyword lambda,
#  so they are also called lambda function 

#  it is a one-line function
#  it can have any number of inputs,but only one expression
#  The Expression is Evaluated and returned when the function is called

#syntax :
# variable_name = lambda arguments : expression 
# print(variable_name())

#eg:

# result=lambda a,b:a+b
# print(result(2,3))




"""MAP FUNCTION"""

# A Map function in python applies a given function to all items in an iterable and return a map object(which is an iterator)
# map(function,iterable)
# Map function is used to apply an expression into a whole type like list,tuple,dict ets  ,its effect all of the values in that type

#eg:
# list1=[1,2,3,4,5]
# result=list(map(lambda a:a**2,list1))
# print(result)


"""FILTER FUNCTION"""

# Filter() function is used on the type like list,dict,tuple etc like that its used to filter the values of the condition aptable
# simple , filter the values means get the values of the condtion true only get the value

# syntax
# filter(function,iterable)

#eg:
# list1=[1,2,3,4,5,6,7,8,9,10]
# result=list(filter(lambda c:c%2 == 0,list1))
# print(result)

























# a=10000

# def ty():
#     a=100
#     # tu=tuple(a)
#     print(a)
#     a+=50
#     print(a)
# ty()

# print(a)