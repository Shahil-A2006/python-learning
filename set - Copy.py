"""set also denoted by {} this curly braces as dictionary"""
"""but the diff from dict is dictionary will key value pairs  but the set is only single values provided"""

# a={}
# print(type(a)) #dict -it the empty will be as taken as dict

"""here we can change the type dict to set of an empty {} by the use of set() function"""
# a={}
# a=set()
# print(type(a)) #<class 'set'>


# a={3}
# print(type(a)) #<class 'set'>




"""set is unoreders thats why we cant get the value with index number - if we try to get value with index it will be error"""

# a={2,5,4,7,9,5,8,0,10}
# print(a[3])  #error - bcoz we cant take with index in set

"""set can't get duplicate values , only show unique values"""

# a={2,5,2,5,7,10}
# print(a)  #{2, 10, 5, 7} -here duplicated values not ghet on the sets



"""imp - set only provide the immutable values means cant changeble values eg:integer ,string,float, boolean , tuple these are immutables"""
"""but we can change the immutable values of above at in the set position we can change at there"""
"""List,Dictionary,Set are not provide inside a set  its be error reason for that bcoz its muttable"""

# s1={15,10,"text",34.5,(1,2,3),True,False}
# print(s1)     #these all types can provide in the set


"""Typecasting - set can allow type-casting"""

# lst= [100,500,"shahil"]
# s1=set(lst)
# print(s1) #{'shahil', 100, 500} -get as set

# tup=(100,500,"shahil")
# s2=set(tup)
# print(s2)  #{'shahil', 100, 500}   -get as set


"""Set Functions"""

"""ADD() - Add only single value when adding, any type can add"""

# s1={1,2}
# s1.add("shahil")
# print(s1) #{'shahil', 1, 2} - it will add anywhere bcoz set is not ordered.


"""update() -used to add multiple values in set - but in list or tuple bcvoz multiple values"""

# s1={1,2}
# s1.update(["shahil",30.5,False])
# print(s1)    #{False, 1, 2, 'shahil', 30.5}  -here add more than one value to the set with the help of update()


# s1={1,2}
# s1.update(("shahil",30.5,False))
# print(s1)   #{False, 1, 2, 'shahil', 30.5} - same but also we can do this with tuple


# lst=[30.5,"shahil"]
# s1.update(lst)
# print(s1)   #{False, 1, 2, 'shahil', 30.5} - here also updating with another way list create first and add that list to set update.


"""remove() - use to remove the value in thne set with the help of their own value"""

# s1={10,100,"text",(1,2,3),True}
# s1.remove(100)
# print(s1)   #{True, 'text', 10, (1, 2, 3)} -here remove the value 100

"""in remove if we put a value that not in the set it will be error"""
# s1={10,100,"text",(1,2,3),True}
# s1.remove(50)
# print(s1)   #error



"""discard() -its the same purpose of remove to remove the value in set but one difference is put a non value in set its not error it wilkl be None"""

# s1={10,100,"text",(1,2,3),True}
# s1.discard(100)
# print(s1)  #{True, 'text', 10, (1, 2, 3)}

"""in discard if we put a value not in the set it will not ann error it will put none"""
# s1={10,100,"text",(1,2,3),True}
# print(s1.discard(50))  #None
 


"""pop() - here in set pop will remove random any value in set ,we cant put a value in pop pop will only provide index we know before but 
in the set case there is no index thats why remove a random value in the set"""

# s1={10,100,"text",(1,2,3),True}

# print(s1.pop()) #True
# print(s1) #{100, 'text', 10, (1, 2, 3)}



"""clear() -used to remove all value in the set ,clear the set in the out will set()"""
# s1={10,100,"text",(1,2,3),True}

# s1.clear()
# print(s1)   #set()


"""copy() - to copy the values of set , its will onordered bcoz its set but all value are in the copied set"""

# s1={10,100,"text",(1,2,3),True}
# s2=s1.copy()
# print(s2)   #{'text', True, 100, 10, (1, 2, 3)}



"""SET OPERATIONS"""

a={1,2,3,4}
b={3,4,5,6}

"""union()-both value in the sets no take duplicates (a | b - is also union())"""

# print(a.union(b))  #{1, 2, 3, 4, 5, 6}
# print(a | b)     #{1, 2, 3, 4, 5, 6}

"""intersection()  -common values in the set (a & b -is also intersection()"""

# print(a.intersection(b)) #{3, 4}
# print(a & b)   #{3, 4}

"""difference() - is the value only in that set no take common and other value of next set"""

# print(a.difference(b)) #{1, 2}  -only values in a
# print(a-b)    #{1, 2}

# print(b.difference(a))  #{5, 6}
# print(b-a)   #{5, 6}


"""symmetric_difference() - the set with removing the common values in the sets"""

# print(a.symmetric_difference(b)) #{1, 2, 5, 6}
# print(a ^ b)   #{1, 2, 5, 6}


"""update is used in here all operators for getting after updating , the values stroed un that variable of set"""
"""this for the three of the operators also"""

# a.intersection_update(b)
# print(a)    #{3, 4}  -  here the value stored as the value into a variable

# a.difference_update(b)
# print(a) #{1, 2} - here the value stored as the value into a variable

# a.symmetric_difference_update(b)
# print(a)   #{1, 2, 5, 6}  - here the value stored as the value into a variable



"""METHODS"""

s1={1,2,3,4,5}
s2={1,2,3}

"""issubset()- to check is it subset of ().  -boolean answers"""
# print(s2.issubset(s1))  #True -s2  values are in s1

"""issuperset()- to check is it superset of (). -boolean answers"""  
# print(s1.issuperset(s2)) #True  - s1 values are in s2

"""isdisjoint()- to check that there is the common value there , if any one value is common its false bcoz its disjoint  -boolean answers"""
# print(s1.isdisjoint(s2))   #False   -there is commonb values in the sets



"""Looping of sets"""

# s1={1,2,3,4,5,"Text"}
# for i in s1:
#     print(i)  #here loop works only in this method cant work eith index means range bcoZ sets cant represent the index



"""Membership operator     -in & not in -to check this value is there in that set"""

s1={1,2,3,4,5,"Text"}
# print(2 in s1)       #True
# print(2 not in s1)   #False


"""FROZEN SET()  - it is for make the set into immutable set (we know that set is muttable but we can change into immutable by using frozenset())"""

# s1 =frozenset({1,2,3})   #we can put here list,tuple or set
# s1.add(10)
# print(s1) #error -bcoz its immutable while it is frozen thats why we cant change anything in there it will be error

 

"""set comprehension     - same as list and dict only change the {} icon of set"""

print({x for x in range(1,11)})   #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print({x for x in range(1,11) if x%2 ==0}) #{2, 4, 6, 8, 10}
