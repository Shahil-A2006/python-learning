"""tuple is denoted in round bracket()"""

#TUPLE

# tu=(1,2,3,4,"python","True")

# print(tu)   #(1, 2, 3, 4, 'python', 'True')
# print(type(tu))  #<class 'tuple'>

# print(tu[0]) #1
# print(tu[1])  #2
# print(tu[-1])  #3


"""if we code like below ones direct value but the out will be tuple"""
# a=1,2,3,4
# print(a)    #(1, 2, 3, 4)
# print(type(a))   #<class 'tuple'>


"""if we code only one value in tuple bracket its typle not be a tuple ,but we can change it into a tuple eg:"""

# b=(10)
# print(type(b))  #<class 'int'>
# c=(10 ,)
# print(type(c))   #<class 'tuple'>  """it is tuple bcoz i add a coma in there at the value"""



"""empty tuple"""
# d=()
# print(type(c))    #<class 'tuple'>

"""slicing"""
# tu=(1,2,3,4,"python","True")
# print(tu[0:3])
# print(tu[ :3])
# print(tu[ : :2])
# print(tu[ : :-1])
# print(tu[-1:-4:-1])


"""tuple is immutable -thats means its cant be change the value in tuple  eg:"""

# tu=(1,2,3,4,"python","True")
# tu[0]=100
# print(tu)   #error will happen bcoz tuple cant immutable


"""here i am itterating with for loop with  direct tuple name and with range"""
# for i in tu:
#     print(i)

# for i in range(len(tu)):
#     print(tu[i])



"""built in functions"""

# tu=(40,10,60,30,20,80,50,90,70,100)
# print(len(tu))  #10
# print(max(tu))  #100
# print(min(tu))   #10
# print(sum(tu))   #550
# print(sorted(tu))  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  -   """here there is no descending order sorting in tuple its only in list"""



"""in the case of alphabets ar are also get the minimum value and the maximum value in a tuple is getting based on asky value"""

a=("a","b","d","c")
# print(len(a)) #4
# print(max(a))  #d
# print(min(a))  #a

"""asky value get by "ord" function"""
# print(ord("a"))  #97
# print(ord("A"))  #65



"""count and index position"""
# tu=(40,10,60,30,10,20,80,50,90,10,70,100)
# print(tu.count(10))  #3
# print(tu.index(60))  #2


"""concatination"""
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2) #(1, 2, 3, 4, 5, 6)
# t3=t1+t2
# print(t3)  #(1, 2, 3, 4, 5, 6)

"""repetition"""
# t1=(1,2,3)
# print(t1*3)  #(1, 2, 3, 1, 2, 3, 1, 2, 3)



"""Unpacking  -means we can assing the values in a tuple into variables after decleration of values  eg:a,b,c """

# tu=(10,20,30)
# a,b,c = tu
# print(a) #10
# print(b) #20
# print(c) #30

"""here while the value are more than variables of variables more than values heppen its an error occured there"""
# tu=(10,20,30)
# a,b = tu
# print(a)  #error
"""we can solve it with (*)-means store multiple values in a variables"""
# tu=(10,20,30)
# a,*b = tu
# print(a)  #10
# print(b) #[20, 30]



"""NESTED TUPLE - Tuple iside a tuple"""

# tu=(5,(3,4),6)
# print(tu[1])      # (3, 4) -1 st index is the second term means (3,4)
# print(tu[1][0])   # 3 here [1] 1st index th[0] th index means the 3 in (3,4)   - [1][1]=4


# """make it one tuple of nested tuple"""
# tu=(5,(3,4),6)
# flat=()

# for i in tu:
#     if isinstance(i,tuple):      #(isinstance is used to check) here check the data inside the tuple , and is it tuple
#         flat += i                   
#     else:
#         flat += (i,)

# print(flat)   #(5, 3, 4, 6)      #here 5 is else , (3,4) is if , 6 is else conditions true  
                                  #here check 2 of both if and else because other other value means iterated values



"""typecasting  - means change one data type to anotehr data type"""

tu=(10,30,45,70,100)
lst=list(tu)
print(lst)   #[10, 30, 45, 70, 100]  - here convert the tuple into list

lst[0]="A"
print(lst)    #['A', 30, 45, 70, 100]  -here change the value is happen bcoz its already convert into list

tu=tuple(lst)
print(tu)      #('A', 30, 45, 70, 100)   -after changing convert  into the tuple   (bcoz changing or modifing is not work in tuple)


"""Membership operator checking - means is it the value is the member in tuple or not in tuple   (boolean answer)"""
"""not in is happen the opp of actual answer whtn the actual ans is true it becomes false"""

tu=(10,20,30,40,"Python","True","Shahil")
print(10 in tu)  #true
print(10 not in tu) #False
print(150 in tu)  #false










