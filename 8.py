#logical operator 
a=5
b=10
if a>b and b>a:
    print("both numbers are greater than 10")
elif a<b or b<a:
    print("atleast one number is less than 5")
elif a!=b:
    print(" a not equal to b")
else:
    print("no")

#comparison operator
age=int(input("enter age:"))
if age>=18 :
    print("you are an adult")
elif age<18:
     print("you are a minor")


#membership operator
s=input("enter string:")
if "a" in s:
    print("yes")
elif "python" not in s:
    print("correct")
else:
    print("no")


#bitwise operator
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)
