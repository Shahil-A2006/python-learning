"""MODULE"""



"""DATE & TIME"""
"""This is buid in module"""


import datetime

# now1 = datetime.datetime.now()
# print(now1)                      #to get current date and time  (use now())

# print(now1.year)                                  #to get the year only
# print(datetime.datetime.now().year)                   #same as get  the year only   with direct above with the varibale

# print(now1.month)                            #to get the month only

# print(now1.day)                    #to get the day only

# print(now1.hour)                   # #to get the hour only

# print(now1.minute)                # to get the minute only

# print(now1.second)                   #to get the second only

# print(now1.microsecond)                  #to get the microsecond only

# print(now1.date())                         #to get the date only  with date (fun)
  
# print(now1.time())                              #to get the time only  with time (fun)


# ------------------------------------------------------------------------------------------------------------

"""STRING FORMAT    -  strft -> its the key for get string format"""

# now =datetime.datetime.now()
# print(now.strftime("%B %d ,%Y"))      #May 19 ,2026     %B-month as str      %d - date      %Y-year    (here strfttime use to get as strformat ,here may)

# ------------------------------------------------------------------------------------------------------------
"""here we set the date ,now() to get current but in below i do that we set the date """
#must we do as the foramt as order (year,month,date)

# birthday=datetime.datetime(2006,12,11)
# print(birthday)        #2006-12-11 00:00:00
# print(birthday.strftime("%B %d ,%Y"))     #December 11 ,2006     ->here do as string format

#--------------------------------------------------------------------------------------------------------------


"""Birthday calculation (age calculate with year)"""

# today=datetime.datetime.now().year
# print(today)
# bday=datetime.datetime(2006,12,11).year
# age = today - bday
# print(age)


#--------------------------------------------------------------------------------------------------------------

x=datetime.datetime(2018,8,5,16,3,45)
# print(x)
# print(x.strftime("%B %d, %Y"))

# print(x.strftime("%A"))                 #to get the day of the week
# print(x.strftime("%a"))                 #to get the abbreviated(short) day of the week

# print(x.strftime("%B"))                         #to get the month name
# print(x.strftime("%b"))                     #to get the abbreviated(short) month name

# print(x.strftime("%d"))                         #to get the day of month as a zero-padded decimal number(eg: 5 -->  05)
# print(x.strftime("%D"))                            # 08/05/18 - to get the date in mm/dd/yy format

# print(x.strftime("%m"))                                  #to get the  month as a zero-padded decimal number(eg: 5 -->  08)

# print(x.strftime("%M"))                 #03       to get the  minute as a zero-padded decimal number(eg: 3 -->  3)

# print(x.strftime("%Y"))                     #2018  - to get the year entire fully
# print(x.strftime("%y"))                       #18 - to get the year of shortly     (2026  ----> 26)

# print(x.strftime("%H"))                  #to get  the hour as zero-paded decimal number in correponding we seted
# print(x.strftime("%I"))                   #to get the hour of actual like we say     (16 --->  4)

# print(x.strftime("%p"))                  #to get the AM/PM based on hour


"""do with aboves"""
x=datetime.datetime.now()
print(x.strftime("%H:%M:%S"))
print(x.strftime("%I:%M:%p"))
        