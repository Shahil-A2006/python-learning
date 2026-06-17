965# 1. Create a tuple with elements: 10, 20, 30, 40. Print the tuple.

# a=(10,20,30,40)
# print(a)

# 2. Write a program to print the first and last elements of a tuple.

# a=(100,200,300,400,500)
# print(f"first element:{a[0]}\nlast element:{a[-1]}")

# 3. Find the length of a tuple using a built-in function.

# a=(100,200,300,400,500,600,700,800,900,1000)
# print(len(a))

# 4. Iterate through a tuple and print each element.

# a=(100,200,300,400,500,600,700,800,900,1000)
# for i in a:
#     print(i,end=" ")

# 5. Check whether the value 50 exists in a tuple.

# a=(100,200,300,400,500,600,700,800,900,1000)
# print(300 in a)

# 6. Write a program to find the sum of all elements in a tuple. (Using for loop too)

# a=(100,200,300,400,500,600,700,800,900,1000)
# print(sum(a))

# s=0
# for i in a:
#     s += i
# print(s)

# 7. Find the maximum and minimum values in a tuple. (Not only using min and max too)

# tu=(25,10,100,50,150)
# x=tu[0]
# y=tu[0]
# for i in tu:
#     if i < x:
#         x = i

#     if i > y:
#         y = i

# print("minimum:", x)
# print("maximum:", y)

# 8. Given the tuple (1, 2, 2, 3, 2), count how many times 2 appears.
# t=(1, 2, 2, 3, 2)
# print(t.count(2))

# x=0
# for i in t:
#     if i == 2:
#         x += 1
        
# print(x)

# 9. Find the index of the element 30 in the tuple (10, 20, 30, 40).

# tu=(10, 20, 30, 40)
# # print(tu.index(30))

# for i in range(len(tu)):
#     if tu[i] == 30:
#         print(i)

# 10. Perform slicing on the tuple (10, 20, 30, 40, 50) to extract the middle elements.

# tu=(10, 20, 30, 40, 50)
# print(tu[2:3])

# 11. Unpack the tuple (100, 200, 300) into variables a, b, and c and print them.

# tu=(100, 200, 300)
# a,b,c = tu
# print(a)
# print(b)
# print(c)

# 12. Use extended unpacking on the tuple (1, 2, 3, 4, 5) to store the first element in one variable and the remaining elements in another list.

# tu=(1, 2, 3, 4, 5)
# a,*b = tu

# print(a)
# print(b)

# 13. Convert a tuple into a list, modify one element, and convert it back to a tuple.

# tu=(10,20,30,40,50)
# lst=list(tu)
# print(lst)

# lst[1]=15
# print(lst)

# tup=tuple(lst)
# print(tup)

# 14. Given a nested tuple t = (1, (2, 3), 4), write a program to access and print the element 3.

# tu = (1, (2, 3), 4)
# print(tu[1][1])

# 15. Concatenate two tuples (1, 2) and (3, 4) and print the result.

# a=(1,2)
# b=(3,4)
# c=a+b
# print(c)

# 16. Repeat the tuple (1, 2) three times and print the result.

# tu=(1,2)
# print(tu*3)

# 17. Write a program to remove duplicate elements from a tuple and create a new tuple.
# tu=(1,2,3,2,4,3,5)
# new=[]

# for i in tu:
#     if i not in new:
#         new.append(i)

# print(tuple(new))

# 18. Reverse a tuple using slicing.

# a=(10,20,30,40,50)
# print(a[ : :-1])

# 19. Sort a tuple and store the result as a new tuple.

# tu=(50,20,30,60,70,100,10,45)
# print(sorted(tu))

# 20. Write a program to find common elements between two tuples.

# a=(20,40,60,100,15)
# b=(25,60,15,55,40)

# for i in a:
#     for j in b:
#         if i == j :
#             print(i)

# 21. Count the frequency of each element in a tuple.

# a=(1,2,3,2,3,4,4,5,6)
# new=[]
# for i in a:
#     if i not in new:
#         print(f"count of {i}: {a.count(i)}")
#         new.append(i)
              
                               
                               
                              
        

# 22. Swap two variables using tuple unpacking without using a temporary variable.

# (a,b)=(10,20)
# print(a) #10
# print(b) #20
# a,b = b,a
# print(a) #20
# print(b) #10

# 23. Given a tuple of strings, find the longest string.

tu=("lion","elephant","dog","tiger","giraffe")
long=0

for i in tu:
    if len(i)>long:
        long=len(i)
        result=i
print(f"longest string: {result}")