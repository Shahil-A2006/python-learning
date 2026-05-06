#Set questions 

""" 1. Create a set with elements: 10, 20, 30, 40. """

# s1={10,20,30,40}
# print(s1)

"""2. Create an empty set and print its type. """

# s1={}
# s1=set()
# print(type(s1))

"""3. Convert the following list into a set: 
       data = [1, 2, 2, 3, 4, 4]    """

# data = [1, 2, 2, 3, 4, 4] 
# s1=set(data)
# print(s1)

"""4. Add the element 50 to a set {10, 20, 30}. """

# set= {10, 20, 30}
# set.add(50)
# print(set)

"""5. Add multiple elements [60, 70, 80] to a set. """

# s1={10,50,100}
# s1.update([60,70,80])
# print(s1)

"""6. Remove element 20 from a set using:
remove()
discard() """

# s1={10,50,20,100,500}
# s1.remove(20)
# print(s1)
# s1.discard(20)
# print(s1)
"""7. What happens if you remove a non-existing element using remove()? Try it."""

#it will be an error
# s1={10,50,20,100,500}
# s1.remove(30)
# print(s1)   #error

"""8. Remove a random element from a set."""

# s1={10,50,20,100,500}
# s1.pop()
# print(s1)

"""9. Clear all elements from a set."""

# s1={10,50,20,100,500}
# s1.clear()
# print(s1)

"""10. Create a copy of a set."""

# s1={10,50,20,100,500}
# s2=s1.copy()
# print(s2)

"""11. Given:
A = {1, 2, 3}
B = {3, 4, 5}
Perform union of A and B. """

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))

"""12. Find intersection of A and B. """

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))

"""13. Find difference (A - B). """

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))

"""14. Find symmetric difference between A and B. """

# a= {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))

"""15. Use operators (|, &, -, ^) for all above operations. """

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)
# print(a & b)
# print(a-b)
# print(a ^ b)


""" 16. Create a set of squares using set comprehension: (numbers from 1 to 5) """

# print({x**2 for x in range(1,6)})

""" 17. Create a set of even numbers from 1 to 20 using comprehension. """

# print({x for x in range(1,21) if x%2 == 0})

""" 18. From a list of numbers, create a set of only odd numbers. """

# print({x for x in range(1,11) if x%2 != 0})

""" 19. Create a set of unique characters from a string: 
     text = "programming" """

# s=set()
# text = "programming"
# for i in text:
#     s.add(i)
    
# print(s)


""" 20. Convert a set into a list and print it. """

# s={10,15,20,25,30}
# lst=list(s)
# print(lst)

