"""   FILE HANDLING   """
"""her i am doing the file hadling with the help of for_example.txt file"""

"""READ MODE-->("r)"""
#read mode is used to read a file content
#if the file is not exist,error raises



# file=open("for_example.txt", "r")
# print(file.read())                      #read the whole file content

# print(file.read(10))                        #read the first 10 characters of the file content

# print(file.readline())                   #read the first line of the file content
# print(file.readline())                      #read the second line of the file content
# print(file.readline())                      #read the third line of the file content

# print(file.readlines())                         #read the whole file content and return a list of line

# print(file.read(2))
# print(file.read(8))

# print(file.tell())                                  #return the current position of the file pointer

# print(file.readline())       #python

# print(file.tell())       #8 - its the pointer by the above line of python and include /n

# print(file.seek(2))   #2       #move the file pointer to the specified pointer
# print(file.readline())   #thon
# print(file.readlines())   #['malappuram\n', 'manjeri\n', 'pullur\n', '\n']

# print(file.tell())
# file.close()
  



"""WRITE MODE--> ("w)"""

#write mode is used to write a file content
#if the file is not exist,it will create a new file


# file=open("hello.txt","w")
# file.write("Hello Guys \n")
# file.write("Python is a programming language \n")
# print(file.read())    #error  - open with write we there cant read there  # not readable
# file.close()

# file1=open("hello.txt","w")
# print(file1.read())       not readable  (error)
# file1.close()

# ----------------------------------------------------------------------------------------------


# file=open("hello.txt","r")
# print(file.read())
# file.close()

# ----------------------------------------------------------------------------------------------


# fi=open("hello.txt","w")
# fi.write("i am shahil")       #here overwrite this content on file hello
# fi.close()

# ----------------------------------------------------------------------------------------------
"""here use this method to add more content into a file otherwise we do more varable here simple method do more with list and add there auto"""

# f=open("hello.txt","w")
# f.writelines(["python \n","java script \n","HTML \n"])        #here writelines used to write the content as list top another file
# f.close()                                                       #its used to add more contents in a file





"""APPEND MODE--> ("a")"""

#append mode is used to append a file content
#if the file is not exist,it will createe a new file



# file=open("for_append.txt","a")
# file.write("Hello guys \n")              #here create a new file that for_append and add the content to there
# file.close()

# ----------------------------------------------------------------------------------------------

# file=open("for_append.txt","a")
# file.write("I am shahil")
# file.write("\nI am 20 Years old \n")
# file.close()

# ----------------------------------------------------------------------------------------------

# file=open("for_append.txt","a")
# file.writelines(["shahil \n","amal \n","ajith \n","arjun \n"])
# file.close()



"""CREATE MODE--> ("x")"""

#create mode is used to create a new file
#if the file is not exist,it will create a new file
#if we call the file already existed file , it will be error bcoz its create mode

# file=open("for_create.txt","x")
# file.write("QUEST INNOVATIVE SOLUTIONS")
# file.close()
#in create  ("x") file not read mode applicable its not possible it will be error




"""READ & WRITE MODE ---> ("r+")"""

#read and write is used to read and write a file content
#if the file is not exist ,error raises    , bcoz priority give to read mode



"""here appening that write the content what we did to the part of that file as existing of start and other add end of writing"""

# file=open("for_example.txt","r+")
# print(file.read())
# file.write("\n ####hello world ####")
# file.write("\n ###")
# file.seek(0)
# file.read()
# file.close




"""WRITE & READ MODE ---> ("w+")"""

#write and read mode is used to write and read a file content
#if the file is not exist,it will create a new file


"""here happen that the content of we write will only pass on the file others remove , overwrite is happening there"""

# file=open("for_example.txt","w+")
# file.write("i am shahil")
# file.close()


# ----------------------------------------------------------------------------------------------

"""IF WE OPEN A FILE WE WOULD CLOSE IT MANUALLY BY file.close() 
 BUT IF WE OPEN THE FILE AT ANOTHER WAY WE COULDNT DO TO CLOSE PYTHON CLOSE IT AUTOMATICALLY (with open ..)arias ->as) -->eg are below how it do"""

# with open("shahil.txt","w") as file1:
#     file1.write("HELLO WORLD,I AM SHAHIL")

# ----------------------------------------------------------------------------------------------

"""CHECK THE FILE IS EXIST OR NOT   (ghet the boolean value --> true or fals"""
"""DO WITH THE HELP OF ---> IMPORT OS  \n print(OS.PATH.EXISTS("FILE"))"""

# import os
# print(os.path.exists("hello.txt"))

# ----------------------------------------------------------------------------------------------

"""RENAME FILE"""
"""to rename a file to another name"""

# import os
# os.rename("intro.py","introduction.py")

# ----------------------------------------------------------------------------------------------
"""DELETE A FILE"""
"""to remove a file"""

# import os
# os.remove("abcd.txt")

# ----------------------------------------------------------------------------------------------

"""TASK"""
#copying a file content to another file by using the file handling?

# with open("for_example.txt","r") as file:
#     fi=file.read()
# with open("higuys.txt","w") as copy:
#     copy.write(fi)

# ----------------------------------------------------------------------------------------------

"""QUESTION"""
"""Write a program that search for a specific word in a file and replace it with another word"""
                                                                                                                   
user1=input("enter a word here: ")
user2=input("enter replaced word here: ")

file=open("hai.txt","r")
change =file.read()
file.close()

change=change.replace(user1,user2)

file=open("hai.txt","w")  
file.write(change)
file.close()

print("changing is successfully completed")



