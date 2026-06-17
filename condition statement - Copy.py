"""from conditional statement"""
# age= int(input("enter your age: "))
# if age>=18:
#     print("You are eligible for voting")
# else: 
#     print("You are not eligible for voting")



# num=int(input("enter the number: "))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")



"""authentication"""
# user="abhi123"
# upass="123456"

# username=input("enter username: ")
# userpass=input("enter password: ")

# if user==username:
#     if upass==userpass:
#         print("authentication succesfull")
#     else:
#         print("incorrect password")
# else:
#     print("incorrect username")



"""nested if"""
# mark=int(input("Enter your mark: "))
# if mark>=90 and mark<100:
#     print("A Grade")
# if mark>=80 and mark<90:
#     print("B Grade")
# if mark>=70 and mark<80:
#     print("C Grade")
# if mark>=60 and mark<70:
#     print("D Grade")
# if mark>=50 and mark<60:
#     print("E Grade")

"""elif"""
# mark=int(input("Enter your mark: "))

# if mark>=90:
#     print("A Grade")
# elif mark>=80:
#     print("B Grade")
# elif mark>=70:
#     print("C Grade")
# elif mark>=60:
#     print("D Grade")
# elif mark>=50:
#     print("E Grade")
# else:
#     print("Failed")

"""print day w.r.t to number 1-7"""
# day=int(input("enter number: "))

# if day==1:
#     print("Sunday")
# elif day==2:
#     print("Monday")
# elif day==3:
#     print("Tuesday")
# elif day==4:
#     print("Wednesday")
# elif day==5:
#     print("Thursday")
# elif day==6:
#     print("Friday")
# elif day==7:
#     print("Saturday")
# else:
    # print("Invalid number")

    
#Ternary operator
# age=18

# result="you are eligible" if age>=18 else "you are not eligible"     #you are eligible
# print(result)

# print("you are eligible" if age>=18 else "you are not eligible")     #you are eligible

# print("even" if 10%2==0 else "odd")   #even


# m=int(input("Enter your mark: "))

# if m>=90:
#     print("A grade")
# elif m>=80:
#     print("B grade")
# elif m>=70:
#     print("C grade")
# else:
#     print("Failed")


name="shahil"
job="devoloper"
age=19

print(name,job,age)
print("iam",name,"iam working as a" ,job," i have",age,"years old")
print(f"iam{name}iam working as a{job}i have {age}years old")