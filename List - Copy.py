# list=[]
# print(type(list))     #<class 'list'>

lst = [50,40,"text",True,30.5,False,"pyhton",10]

# print(lst)  #[50, 40, 'text', True, 30.5, False, 'pyhton', 10]
"""check the value using index number"""
# print(lst[4])  #30.5
# print(lst[-2])  #false

"""can change the value using index here replacing"""
lst[1]=100
print(lst)  #[50, 100, 'text', True, 30.5, False, 'pyhton', 10]

print(len(lst)) #8


"""Type casting can use in here means date type can change us means(tuple to list ,list to tuple    /eg are below)"""

tu=(1,2,3)
print(list(tu))  #[1, 2, 3]      -here tuple change into list
print(tuple(lst)) #(50, 100, 'text', True, 30.5, False, 'pyhton', 10)   - here list change to tuple


lst = [50,40,"text",True,30.5,False,"pyhton",10]

"""list also we can splice the values from there"""
print(lst[0:5]) #[50, 40, 'text', True, 30.5]     - here get with splicing 0 to 5 indexed values
print(lst[4:7])   #[30.5, False, 'pyhton']         -   here get with splicing 4 to 7 indexed values

"""here we check the value in the list"""
print(30.5 in lst)   #True


"""here using append to Add any values to the end of the list"""
lst = [50,40,"text",True,30.5,False,"pyhton",10]
lst.append("shahil")
print(lst)   #[50, 40, 'text', True, 30.5, False, 'pyhton', 10, 'shahil']

"""here using extend also Add at the end of list but one diff that is each alpha or character can take seperatly   eg:"""
lst.extend("hello")
print(lst)   #[50, 40, 'text', True, 30.5, False, 'pyhton', 10, 'shahil', 'h', 'e', 'l', 'l', 'o']




"""but extend is used to join the two different list as one list eg:"""
lst1=[10,20,"shahil,True",50]
lst2=[100,200,300,"python"]

"""if append it it will add at the end but as a another list inside there but extend is not like that"""
# lst1.append(lst2)
# print(lst1)   #[10, 20, 'shahil,True', 50, [100, 200, 300, 'python']]

"""here extend the two different list into one list as proper using extend"""
# lst1.extend(lst2)
# print(lst1)   #[10, 20, 'shahil,True', 50, 100, 200, 300, 'python']


"""insert - is used to add any value to a index position ehat we did   ,eg:"""
# lst1.insert(1,"shahil")
# print(lst1)   #[10, 'shahil', 20, 'shahil,True', 50, 100, 200, 300, 'python']



"""remove -is used to remove a value in list by using that value"""
# lst=[100,200,300,400,500,"python","shahil"]
# lst.remove(200)
# print(lst)

"""pop - it is also used to remove the value in list but one diif is here remove  the index numbered value we put index number to remove"""
"""if only put pop the last value will remove"""
# print(lst.pop())  #shahil  -the value of poped
# print(lst.pop(2))  #400     -the value of poped
# print(lst)    #[100, 300, 500, 'python']   -here the out with poped means removed after list bcoz we print as seperate list 


"""clear-used the clear all values in a list and becomes into a empty list"""
# lst.clear()
# print(lst)    # [] -this is the output



"""index()-used to get the index position of the value"""
lst = ["shahil","shanoon",100,"fathima beevi", 500,"ashraf"]
# print(lst.index("shanoon"))  #1
# print(lst.index("ashraf"))    #5
# print(lst.index("python"))    #error will happen bcoz this value is no in that list



"""count the value is how many times are there in the list"""
# lst = ["shahil","shanoon",500,100,"fathima beevi", 500,"python","mac",500]
# print(lst.count(500)) #3 - 500 is 3 times in the list





"""sort- is used to arrange the ascending order  -sort()"""
"""if we want to order as descending order do sort(reverse=True)"""

lst1=[200,30,1000,10,15,5,45]
# lst2=["z","c","b","a","x"]

# lst1.sort()
# print(lst1)  #[5, 10, 15, 30, 45, 200, 1000] -order as ascending

# lst2.sort()
# print(lst2)  #['a', 'b', 'c', 'x', 'z'] -order as ascending

"""here i am reversing it do descending by reverse=True"""
# lst1.sort(reverse=True)   #[1000, 200, 45, 30, 15, 10, 5]   - order as descenfing
# print(lst1)

# lst2.sort(reverse=True)   #['z', 'x', 'c', 'b', 'a']  - order as descenfing
# print(lst2)




"""reverse - is used to reverse the entire list """
# lst=["quest",20,"python","shahil",50]
# lst.reverse()
# print(lst)    #[50, 'shahil', 'python', 20, 'quest']




"""copy -used to same purpose of copy the same copied list is print in output"""
# list10=lst.copy()
# print(list10)



"""here functions applicable to that function named purpose ,eg:sum-use to sum"""

# li=[10,20,30,100,500,200]
# print(len(li))       #6  -length of list
# print(sum(li))       #860 -sum of list
# print(min(li))        #10 -min value of list
# print(max(li))        #500 -max value of list






"""Here i am looping means iterating the list using direct list name and the index value with range"""
list=[10,20,30,"python","shahil",200,"quest"]

# for i in list:
#     print(i)
 
# for i in range(len(list)):
#     print(list[i])


"""list comprehension"""

# a=[x for x in range(1,11) if x%2==1]
# print(a)

# a=[i**2 for i in range(1,11) if i%2==0]
# print(a)

# lst=["even" if x%2==0 else "odd" for x in range(1,11)]
# print(lst)

"""nested list"""

# x=[[1,2],[3,4]]
# print(x[0][1])

# for i in x:
#     for j in i:
#         print(j, end=" ")
#     print()


"""shallow copy and deep copy""" """......................for nested list only"""

# import copy
# lst= [[1,2,3],[4,5,6]]

# lst1=copy.copy(lst)
# lst2= copy.deepcopy(lst)
# lst[0][1]=99

# print(lst)
# print(lst1)
# print(lst2)


"""for user input list with limit"""

# lst=[]
# rng= int(input("enter list range: "))
# for i in range(rng):
#     a= input(f"enter {i+1} value: ")
#     lst.append(a)
# print(lst)







  