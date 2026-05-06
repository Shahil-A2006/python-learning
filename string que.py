# 1.Take a string as input and print its length.

# a=input("Enter a string= ")
# print(len(a))

# 2.Reverse a string.

# a="shahil"
# print(a[-1: :-1])

# 3.Print the first and last character of a string.

# a="QEUST INNOVATIVE SOLUTIONS"
# print(a[0] , a[-1])


# 4.Convert a string to uppercase.

# a="i am Shahil"
# print(a.upper())

# 5.Convert a string to lowercase.

# a="INDIA is my country"
# print(a.lower())

# 6.Count the number of vowels in a string.

# a="india is my country"
# z=0
# for i in a:
#     if i in "aeiouAEIOU":
#         print(i)
#         z+=1
# print(z)

# 7.Check whether a string is a palindrome.

# string = input("Enter a string: ")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#using loop

# a="malayalam"
# rev=""
# for i in a:
#   rev = i+rev 
# if a == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 8.Remove all spaces from a string.

# a="india is my country"
# b=""
# for i in a:
#     if i != " ":
#         b+=i
# print(b)

# 9.Check whether a particular character exists in a string.

# string = input("enter a string: ")
# char =input("enter a particular character:")

# if char in string:
#     print("Character exists")
# else:
#     print("Character does not exist")

# 10.Count how many times a character appears in a string.

# string = "hello world"
# char = "l"
# count = 0

# for ch in string:
#     if ch == char:
#         count += 1

# print("Count:", count)



# 11.Count the number of words in a string.

# a="india is my country"
# b=a.split()
# print(len(b))


# 12.Find the longest word in a sentence.

# a="india is my country"
# lst=a.split()
# max=len(lst[0])
# word=lst[0]
# for i in lst:
#     if max < len(i):
#         word = i
# print("longest word :",word)

# 13.Remove duplicate characters from a string.

# text = "i am shahil"
# ans = ""

# for a in text:
#     if a not in ans:
#         ans += a

# print(ans)


# 14.Remove all vowels from a string.

# a="quest innovative solutions"
# b=""

# for i in a:
#     if i.lower() not in "aeiou":
#         b += i

# print(b)


# 15.Reverse a string using a loop (without slicing).

# a="shahil"
# b=""

# for i in a:
#     b=i + b

# print(b)
# 16.Print only uppercase letters from a string.

# text = "INDIA is MY country"

# for i in text:
#     if i.isupper():
#         print(i, end="")
# 17.Extract only digits from a string.

# a="abcd2345"
# b=""

# for i in a:
#     if i.isdigit():
#         b += i

# print(b)

# 18.Convert a string to title case manually (without using built-in functions).

# a="india is My country"
# print(a.wtitle())

# 19.Find the first non-repeating character in a string.

# a="india is my country"
# b=""

# for i in a:
#     if a.count(i) == 1:
#         b = b+i
# print(b)


# 20.Replace spaces in a string with underscores (_).

# a="My name is shahil"
# print(a.replace(" ","_"))





# 21. Take two strings and check it is anagram or not 


# a = "eat"
# b = "ate"

# if len(a)==len(b):
#     for i in a:
#         if i not in b:
#             print("not anagram")
#             break
#     else:
#         for j in b:
#             if j not in a:
#                 print("not anagram")
#                 break
#         else:
#             print("anagram")



# 22.Most frequently used character in a string    

# a="my name is shahil"
# max=0
# ch=""
# for i in a:
#     if max <a.count(i):
#         max = a.count(i)
#         ch = i

# print(ch)




# 23.Return index no:of first unique character in a string 


# a="india is my country"
# for i in a:
#     if a.count(i) ==1:
#         print(i)
#         break



a=[10,20,30,40,50,60,70,80,90,100]
max=0

for i in a:
  if  i>max:
    max=i
print(max)



# num=int(input("enter a number: "))

# for i in range(1,num):
#     if num%1 == 0:
#         print("its not a prime number")
#     else:
#         ("its a prime number")