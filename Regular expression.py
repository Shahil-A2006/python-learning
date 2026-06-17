"""finding matches....................................."""
# import re 
# data='hi good morning'
# x=re.findall('[a-g]',data)      #return letters between a-g including a&g
# print(x)

# import re
# txt='hello abhi'
# x=re.findall('he...',txt)           #return words starts with 'he' and have length 5
# print(x)

"""startwith matches............................."""
# import re
# txt='the earth is very big'
# x=re.findall('^th',txt)             #return sentence starts with 'th' (can check multiple line with 're.M' after the varibale)
# if x:
#     print('yes it statrts with "th" ')
# else:
#     print('no match')
# print(x)

"""ends with....................."""
# import re
# txt='the earth is very big'
# x=re.findall('ig$',txt)             #return sentence ends with 'ig'
# if x:
#     print('yes it ends with "ig" ')
# else:
#     print('no match')
# print(x)

"""zero or more occurance......................"""
# import re
# txt='the earth is very big, eat it'
# x=re.findall('ea*',txt)             #return all occurance with 'e' and 'a', occurance of 'a' can be zero or more
# if x:
#     print('have matches')
# else:
#     print('no match')
# print(x)

"""one or more occurance......................"""
# import re
# txt='the earth is very big, eat it'
# x=re.findall('ea+',txt)             #return all occurance with 'e' and 'a', occurance of 'a' can be one or more
# if x:
#     print('have matches')
# else:
#     print('no match')
# print(x)


"""start with letter........................."""
# import re
# txt="the real world"
# x=re.findall(r'\Athe',txt)           #\A return sentence starts with 'the'
# print(x)


"""check a word/letter followed by a letter.........................."""
# import re
# txt="in india rain can gain by main weather"
# x=re.findall(r'\Bain',txt)           #\B return sentence ends/followed as 'ain'
# print(x)


"""finding digits..............."""
# import re
# t='vjv652w 72e67vvd 76589h'
# x=re.findall(r'\d',t)               #return all digits
# print(x)


"""finding all non-digits..................."""
# import re
# t='vjv652w 72e67vvd 76589h'
# x=re.findall(r'\D',t)               #return all non-digits
# print(x)


"""finding space........................"""
# import re
# t='vjv652w 72e67vvd 76589h'
# x=re.findall(r'\s',t)               #return all space
# print(x)


"""finding all characters........................"""
# import re
# t='vjv652w 72e67vvd 76589h'
# x=re.findall(r'\S',t)               #return all character exclude space
# print(x)


"""finding alphabet & digits........................"""
# import re
# t='vjv652w 72e67vvd 76589h'
# x=re.findall(r'\w',t)               #return all exculde space and special characters
# print(x)


"""finding space and special character........................"""
# import re
# t='vjv652w 72e67@vvd 76589h'
# x=re.findall(r'\W',t)               #return all space and special characters
# print(x)


"""ends with - (\Z)  & ($)"""

# import re
# t="i am shahil"
# x=re.findall(r"l\Z",t)       #['l']
# print(x)
#--------------------------------------------------------------------
# import re
# t="i am shahil\n"
# x=re.findall(r"l\Z",t)       #[]              #consider \n , thats why its empty
# print(x)

#--------------------------------------------------------------------

# import re
# t="i am shahil"
# x=re.findall(r"l$",t)       #['l']       
# print(x)
#--------------------------------------------------------------------
# import re
# t="i am shahil\n"
# x=re.findall(r"l$",t)       #['l']        #not considet \n , thats why get last ends with
# print(x)

#--------------------------------------------------------------------


"""finding words with specific length................................"""
# import re
# t='hi there good morning, helllo.hemmmo'
# x=re.findall('he.{3}o',t)              #return words 'he'+ 3 chara+ 'o' 
# print(x)

#--------------------------------------------------------------------


"""checking either charcters present.........................."""
# import re
# t='hi there good morning, helllo.hemmmo'
# x=re.findall('[omg]',t)              #return characters o/m/g
# print(x)

#--------------------------------------------------------------------

"""to print digits"""

# import re
# t="mom23 45687 hello 10"
# x=re.findall(r"\d",t)        #het by one by one  (/d)
# print(x)                            #['2', '3', '4', '5', '6', '8', '7', '1', '0']

#--------------------------------------------------------------------


# import re
# t="mom23 45687 hello 10"
# x=re.findall(r"\d+",t)             #here get by like continues numbers (d+)
# print(x)                       #['23', '45687', '10']



"""here also get digits but do with setting range and select that patterns """

# import re
# t="8 times before 11;45 AM 67890 112 hyderabad 1234"
# x=re.findall("[0-9]",t)                                #check if the string contains 0-9
# print(x)                                  #['8', '1', '1', '4', '5', '6', '7', '8', '9', '0', '1', '1', '2', '1', '2', '3', '4']

#--------------------------------------------------------------------

# import re
# t="8 times before 11;45 AM 67890 112 hyderabad 1234"
# x=re.findall("[0-9]+",t)                                #select all the continues numbers
# print(x)                                            #['8', '11', '45', '67890', '112', '1234']



"""check if the string has two digit number from 00 to 59"""

# import re
# t="67 abc 451617hha 2342455 90 abc"
# x=re.findall("[0-5][0-9]",t)                # get the value btw what we set the range , here it is 00 to 59
# print(x)                                 # ['45', '16', '17', '23', '42', '45']

#--------------------------------------------------------------------

"""replace all whitespace with * """

# import re
# a="i am shahil i am a student"
# x=re.sub("\s","*",a)          # here replace * on white space to do that /s , if we want to change another anything put that on yhe place \s
# print(x)                      # i*am*shahil*i*am*a*student

#--------------------------------------------------------------------
