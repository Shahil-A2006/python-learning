# for i in range(10):
#     for j in range(10):
#         print(j,end=" ")
#     print()

# output
# 0 1 2 3 4 5 6 7 8 9 
# 0 1 2 3 4 5 6 7 8 9 
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9


# for i in range(1,10):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# output
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9


# for i in range(10,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# output
# * * * * * * * * * *
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *




# questions


# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

# * * * * 
# * * * * 
# * * * *
# * * * *


# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4 


# x=1
# for i in range(4):
#     for j in range(4):
#         print(x,end=" ")
#         x += 1
#     print()

# output
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12
# 13 14 15 16


# x=5
# for i in range(3):
#     for j in range(3):
#         print(x,end=" ")
#         x += 5
#     print()

# output
# 5 10 15 
# 20 25 30 
# 35 40 45 


# x=100
# for i in range(5):
#     for j in range(5):
#         print(x,end=" ")
#         x += 100
#     print()

# output
# 100 200 300 400 500
# 600 700 800 900 1000
# 1100 1200 1300 1400 1500
# 1600 1700 1800 1900 2000
# 2100 2200 2300 2400 2500


# for i in range(4):
#     for j in range(4):
#         if i%2 == 0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# output
# 1 1 1 1 
# 0 0 0 0 
# 1 1 1 1 
# 0 0 0 0 



# for i in range(4):
#     for j in range(4):
#         if j%2 == 0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# output
# 1 0 1 0 
# 1 0 1 0 
# 1 0 1 0 
# 1 0 1 0 



# x=1
# for i in range(2):
#     for j in range(4):
#         print(x,end=" ")
#         x += 1
#     print()

# output
# 1 2 3 4 
# 5 6 7 8 



# for i in range(4):
#     for j in range(4):
       
#         if i == 0 or i == 3 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()     

"""
output
 * * * * 
 *     * 
 *     * 
 * * * * 
"""


# for a in range(1,4):
#     for b in range(a):
#         print(b+1,end=" ")
#     print()

"""
1
1 2
1 2 3
"""


# x=1
# for a in range(1,4):
#     for b in range(a):
#         print(x,end=" ")
#         x += 1
#     print()

"""
1
2 3
4 5 6
"""

# for a in range(1,4):
#     for b in range(a):
#         print(a,end=" ")
#     print()

"""
1
2 2
3 3 3
"""

# for a in range(1,5):
#     for b in range(a):
#         if b%2==0 :
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

"""
output
1 
1 0 
1 0 1 
1 0 1 0 
"""



# for a in range(6,0,-1):
#     for b in range(a):
#         print("*",end=" ")
#     print()

"""
output
* * * * * * 
* * * * * 
* * * *
* * *
* *
*

"""


