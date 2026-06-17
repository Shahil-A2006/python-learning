"""DICTIONARY  -  {}  """
"""dictionary is unorederd pair today always.at 3.6 until its orederd"""
"""stored a key value pair (key value is uniqueif key value repeated,the data will overrides)"""
"""dictionary is mutable"""
"""the valuye can get by accessing the key"""

# di={}
# print(type(di))   #<class 'dict'>

# di={"a":1,"b":2,"c":3}
# print(di)


"""access the value with key  - if we type same two keys it will over rides the valu of lasts   eg:"""

# di={"a":1,"b":2,"c":3,"a":7}   #{'a': 7, 'b': 2, 'c': 3}
# print(di)

# di={"a":1,"b":2,"c":3}
# print(di["b"])   #2   - the value of b


"""empty dictionary"""
# di={}
# print(di) #{}


"""dictionay is mutable means we can change the values with the help of their keys"""

# dic={"name":"shahil" , "place":"manjeri"}
# print(dic["name"]) #shahil

# dic["name"]="shanoon"
# print(dic["name"]) #shanoon

# print(dic)    #{'name': 'shanoon', 'place': 'manjeri'}



"""here we do like type casting do a tuple  change into dictionary like below ones eg:"""

# d=dict(a=1,b=2)
# print(d)      #{'a': 1, 'b': 2}  - its out is dictionary


"""here the get()-function also for acces the value with key but one change is that while we access the value dirct if there we put a non value in dic its be error but we put non value in get() function is to be none"""

# di={"a":1,"b":2,"c":3}
# print(di["a"])  #1
# print(di["d"])  #error - bcoz there is no d key in the dic

"""get()"""
# print(di.get("a")) #1
# print(di.get("d"))   #none - none will be put when not a value in dic put in get()
# print(di.get("d"),"shahil")  #None shahil    -after get , then what we put it will be out after None



"""udating - change value there"""

# detail={"name":"shahil","mark":80}

# detail["mark"] = 90
# print(detail)  #{'name': 'shahil', 'mark': 90}



"""adding - the key value to the dictionary of last when we put the key and value not in the dictionary"""

# detail={"name":"shahil","mark":80}

# detail["place"]="manjeri"
# print(detail)  #{'name': 'shahil', 'mark': 80, 'place': 'manjeri'}  - place is added there bcoz it has not in the dic


"""POP - remove the elements in a dic (in list we pop with undex here with key name)"""

detail={'name': 'shahil', 'mark': 80, 'place': 'manjeri'}
# print(detail.pop("name"))  #shahil   - poped value
# print(detail)           #{'mark': 80, 'place': 'manjeri'}   -after poped dictionary

"""popitem() - is to remove the last elemenmt in the dictionary"""
# detail.popitem()
# print(detail)   #{'name': 'shahil', 'mark': 80} - last item is poped

"""del  - delete - its the same purpose of clear to remove the element in the dic"""
# del detail["name"]
# print(detail)  #{'mark': 80, 'place': 'manjeri'}

# del detail
# print(detail)  #error -there is no that named thing like is happen here (remove the entire dic)


"""clear - to get the empty dictionary """
# detail.clear()
# print(detail)    #{}



"""Looping the dic """
"""normaly when i am loop only get key    also key get with keys()-function"""
"""i want the value to iterate i will use the value()-function       dic[i]"""
"""when i want both key and value do two variable for both i,j then use items()-functions    then call i and j"""

dic={"a":1,"b":2,"c":3}
"""loop keys"""
# for i in dic:
#     print(i ,end=" ")   #a b c

# for i in dic.keys():
#     print(i ,end=" ")  #a b c

"""loop value"""
# for i in dic.values():
#     print(i ,end=" ")   #1 2 3 

# for i in dic:
#     print(dic[i] ,end=" ")   #1 2 3  - here also get value with dic[i]-means we do dic[a] get the value of a ,,,,here we do get the value of i , i is iterated the whole dictionary thates why get the whole value of dic

"""loop key and value"""

# for i,j in dic.items():
#     print(i,j ,end=" ")  #a 1 b 2 c 3    - here we get the key and value with the items()-function and call both variables  , if we call one get thats value


"""here i do to only get keys and only het values and both of two of in whole dic but to an iterating and also it will like at list"""
"""here type is dic always but output only like list to see"""

# di={'name': 'shahil', 'mark': 80, 'place': 'manjeri'}
# print(di.keys())  #dict_keys(['name', 'mark', 'place'])  - get only keys but in list
# print(di.values())  #dict_values(['shahil', 80, 'manjeri']) - get only values but in list
# print(di.items())   #dict_items([('name', 'shahil'), ('mark', 80), ('place', 'manjeri')]) - get both key and value but in list


"""update the value with key we do above also there is a functions update() also use to update any key value"""

# di={'name': 'shahil', 'mark': 80, 'place': 'manjeri'}
# di["mark"]=100
# print(di)   #{'name': 'shahil', 'mark': 100, 'place': 'manjeri'}

# di.update({"mark":100})
# print(di)    #{'name': 'shahil', 'mark': 100, 'place': 'manjeri'}  - here update with the update()-function

"""copy - to copy the dictionary"""

# di={'name': 'shahil', 'mark': 80, 'place': 'manjeri'}
# s1=di.copy()
# print(s1)  #{'name': 'shahil', 'mark': 80, 'place': 'manjeri'} -here the same bcoz we copy this


"""setdefault - is used to when that key in there it line will ignoe by python if the key is no in there it will add there at the end"""

# di={'name': 'shahil', 'mark': 80, 'place': 'manjeri',"grade":"A"}
# di.setdefault("grade","C")
# print(di)    #{'name': 'shahil', 'mark': 80, 'place': 'manjeri', 'grade': 'A'} -
"""above get the same dic bcoz the setdefault is ignore the grade c bcoz there is already grade key in there thats why not change there other wisew the key is not in there in will update"""

# di={'name': 'shahil', 'mark': 80, 'place': 'manjeri'}
# di.setdefault("grade","C")
# print(di)   #{'name': 'shahil', 'mark': 80, 'place': 'manjeri', 'grade': 'C'} - here add the grade with help of set defaulkt bcoz there is no already the grade key


"""fromkeys()- function is used to store the value what we did to the entire keys in the dict"""
a=["a","b","c"]
# b=dict.fromkeys(a,10)
# print(b)


"""NESTED DICTIONARY - here nested dic denote with a value here eg:s1,s2"""

# di={
#      "s1":{"name":"shahil","age":19},
#     "s2":{"name":"shanoon","age":25}
# }

# print(di["s1"])  #{'name': 'shahil', 'age': 19}

# print(di["s1"]["name"]) #shahil

# print(di["s2"]["age"])  #25


"""DICTIONARY COMPREHENSION  - Its used to iterate in the single line"""

# for i in range(1,11):
#     print(i)                         #here loop work in normal but in dict there is comprehention there by here eg at single line

# print({x:x for x in range(1,11)})   #{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}  - here iterate in by dict comprehension

# print({i:i*i for i in range(1,11)})   #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# print({i:i**2 for i in range(1,11)})   #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# print({x:x for x in range(1,11) if x%2 == 0})   #{2: 2, 4: 4, 6: 6, 8: 8, 10: 10}

# print({x:"even" for x in range(1,11) if x%2 == 0})  #{2: 'even', 4: 'even', 6: 'even', 8: 'even', 10: 'even'}


"""MEMBERSHIP OPERATOR"""
"""here key is defaultly check thats why we can direct key in dic thias way can check but value check with values fun()"""


# di={"a":1,"b":2,"c":3,"d":4}

# print("c" in di) #True 

# print(2 in di.values()) #True


"""MERGING (|) - HERE merging two dict ,merge use with the pipe-line simple(|)"""

# s1={"a":10}
# s2={"b":20}
# d3=s1 | s2
# print(d3)   #{'a': 10, 'b': 20}


"""SORTING"""

dic={"b":3,"c":2,"a":1,"d":4}

print(sorted(dic))  #['a', 'b', 'c', 'd'] - we only get defaultly sort keys only dont get both key andd value bcoz a=2 whtich we can sort only key

print(sorted(dic.keys())) #['a', 'b', 'c', 'd'] -  here sort the keys with key fun(same as default dic sorted out)

print(sorted(dic.values()))  #[1, 2, 3, 4]  - here sort onlyu value by val fun()



















"""out of sylllabus"""
"""dir(-directry is used to know what functions are that in this"""
"""print(dir(dic))    -#here we get the functions in the dic"""   



