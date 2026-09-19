age=int(input("enter age:"))
female=input("are you a female(true\false):").lower()
if age==5:
    print("bus pass is free")
elif age>5 and age<=18:
    print("you pay the bus price")
elif age>=60:
    print("you are eligible for senior citizen discount")
elif age>=18 and female=="true":
    print("you are eligible for female discount")
else:
    print("you are not eligible for any discount")
