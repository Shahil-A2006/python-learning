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
        
