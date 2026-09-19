time=int(input("enter time:"))
if time>8 and time<=10:
    print("it's a breakfast time")
elif time>11 and time<=15:
    print("it's a lunch time")
elif time>=20 and time<=22:
    print("it's a dinner time")
else:
    print("it's not a meal time")
#_______________________________________________________________________________________________________
age=int(input("enter age:"))
print("person is eligible for library membership!!")
if age>10 and age<=18:
    print("student membership!")
elif age>60:
    print("senior citizen membership!")
else:
    print("they get a regular membership")
