"""Dictionary qns"""

""" 1. Create a dictionary with keys: name, age, course and assign values"""

# details={"name":"shahil","age":19,"course":"python"}
# print(details)

""" Print the value of name from a dictionary """

# details={"name":"shahil","age":19,"course":"python"}
# print(details["'name'"])

""" 3. Add a new key mark with value 85 to an existing dictionary """

# details={"name":"shahil","age":19,"course":"python"}
# details["mark"] = 85
# print(details)

""" 4. Update the value of age to 25 """

# details={"name":"shahil","age":19,"course":"python"}
# details["age"] = 25
# print(details)

""" 5. Remove a key course from a dictionary """

# di={"name":"shahil","age":19,"course":"python"}
# di.pop("course")
# print(di)

""" 6. Use get() to safely access a key that may not exist. """

# di={"a":1,"b":2,"c":3}
# print(di.get("c"))

# print(di.get("d","not exist"))

""" 7. Print all keys in a dictionary. """

# di={"a":1,"b":2,"c":3}

# print(di.keys())

# for i in di:
#     print(i)


""" 8. Print all values in a dictionary. """

# di={"a":1,"b":2,"c":3}

# print(di.values())

# for i in di.values():
#     print(i)

""" 9. Print all key-value pairs using items(). """

# di={"a":1,"b":2,"c":3}

# print(di.items())

# for i in di.items():
#     print(i)

""" 10. Find the length of a dictionary. """

# di={"a":1,"b":2,"c":3,"d":4}
# print(len(di))

"""11. Write a program to check if a key exists in a dictionary. """

# di={"a":1,"b":2,"c":3,"d":4}
# print("c" in di)

""" 12. Create a dictionary and use a loop to print all keys and values. """

# di={"a":1,"b":2,"c":3}

# for i in di.items():
#     print(i)

""" 13. Copy one dictionary into another. """

# di={"a":1,"b":2,"c":3}
# s1=di.copy()
# print(s1)

""" 14. Use setdefault() to add a key only if it doesn't exist. """

# di={"name":"shahil","age":19,"course":"python"}
# di.setdefault("gender","men")
# print(di)

""" 15. Merge two dictionaries. """

# a={"a":1,"b":2,"c":3}
# b={"c":4,"d":5,"e":6}
# c=a | b
# print(c)

""" 16. Remove the last inserted item using a method. """

# a={"a":1,"b":2,"c":3}
# a.popitem()
# print(a)

""" 17. Clear all items from a dictionary. """

# a={"a":1,"b":2,"c":3}
# a.clear()
# print(a)

""" 18. Convert dictionary keys into a list. """

# details={"name":"shahil","age":19,"course":"python"}
# x=list(details)
# print(x)

""" 19. Create a dictionary using fromkeys() with default value 0. """

# di=["a","b","c","d"]
# b=dict.fromkeys(di,0)
# print(b)

""" 20. Sort dictionary keys and print them.  """

# dic={"name":"shahil","age":19,"course":"python"}
# print(sorted(dic.keys()))


# 21. Count frequency of each character in a string using dictionary.
# 22. Count frequency of words in a sentence.
# 23. Create a nested dictionary for students (name, age, marks).
# 24. Access values from a nested dictionary.
# 25. Write a program to find the key with maximum value.
# 26. Write a program to invert a dictionary (swap keys and values