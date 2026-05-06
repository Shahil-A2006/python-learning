"""indexing"""

# a="abcde"
# print(len(a))
# print(a[-1])

"""docstring"""

# x= """hi there
#     im shahil A, an aspiring python fullstack develepor"""
# print(x)

"""slicing"""

# a="python"
# print(a[0:3]) 
# print(a[0:])
# print(a[0:5:2]) 
# print(a[::2])
# print(a[5::-1])
# print(a[::-1])
# print(a[-1:-7:-1])

"""string function"""

"""case function"""
a= "hI tHeRE i AM AbhiNAnd"
# print(a.lower())
# print(a.upper())
# print(a.capitalize())
# print(a.title())
# print(a.swapcase())

"""alignment & formatting"""
a="hi there"
b="xxxx"
# print(a.center(12)+b)
# print(a.ljust(12)+b)
# print(a.rjust(12)+ b)
# print(a.zfill(12))




#searching function

a="python programming"
# print(a.find("n"))  #first match index position
# print(a.index("y")) #first match index position if not found shows error
# print(a.rfind("m"))  #search from right side catch first matches from right
# print(a.count("p"))  #to show count


#boolean ans function

# a="python123"
# print(a.isalnum()) # isalnum- check alphabet number ///// true bcoz there is only albha and number no special character
# print(a.isalpha())  # isalpha -check alphet only     ////false bcoz there are digits also
# print(a.isdigit())  # isdigit -check only digits     //// false bcoz there are alphates also

# a="python"
# print(a.islower()) #islower -check it's a lower cased string   ////true bcoz its lower cased 
# print(a.isupper()) #isupper-check it,s a upper cased string    ////false bcoz its not upper cased
# print(a.isspace()) #isspace-check there is only space in string  ////false bcoz there is no only space in it

# print(a.startswith("p")) #startswith-check is it strats with this   ////true bcoz string starts with p
# print(a.endswith("n"))  #endswith-check is it ends with this     ////true bcoz it's ends with n



#Replace

# a="hello world"
# print(a.replace("world","shahil"))  #hello shahil          (which we change , what replace there)


#split     -to split other by other

# a="india is my country"
# print(a.split())   #['india', 'is', 'my', 'country']   -here only split() thats why split by space be occur

# a="india_is_my_country"
# print(a.split("_"))  #['india', 'is', 'my', 'country']  -also split by underscore


#partition  - split but only what we considered first only that split others that also print there

# a="hello-world-python"
# print(a.partition("-")) #('hello', '-', 'world-python')
# print(a.rpartition("-")) #('hello-world', '-', 'python')

# #join  - join to a one string

# a=["iam","shahil","iam studied","in quest"]
# print(" ".join(a))   #iam shahil iam studied in quest       -here join all substring into a single string


#strip - to avoid unwanted spaces in startring and at ending only

# a="     hello world     "
# print(a.strip()) #avoid space in lest and right
# print(a.lstrip()) #avoid space only in leftside
# print(a.rstrip()) #avoid space only in rightside


#encoding

# a="hello"
# print(a.encode())  #b'hello'


#format string  - to join contents

# a="shahil"
# print(f"My Name is {a}")



#escape sequance   (\n , \t , \b , \)

# print("hello \nworld") # \n-new line
# print("hello\tworld")  # \t-tabspace
# print("hello \bworld") # \b-backspace

# print("\"india\" is my country")  # \ -ignore in codes but run by that what we enter 


#length -to get the length of the string

a="python"
# print(len(a))  #6
# print(len("pyhton"))  #6


#looping

# a="python programming"
# for i in a:
#     print(i,end=" ")


#string membership operator    (in , is)  - check is it there in that string
# a="python programming"
# print("py" in a)  #true   

# """vowel checking"""
# a="python programming"
# for i in a:
#     if i in 'aeiouAEIOU': 
#         print(i)









a="shahil"
for i in a:
    if i in "aeiou":
        print(i)