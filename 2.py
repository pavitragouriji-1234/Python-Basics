a="2"
b="4"
print(int(a))
print(int(b))
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)/int(b))
print(int(a)//int(b))
print(int(a)%int(b))

#_________________________________________________________________________________________________________

p=float(input("enter number:"))
print(p)
p1=int(p)
print(p1)
print("data type of p is:",type(p))
print("data type of p1 is:",type(p1))

#________________________________________________________________________________________________________

s="12345"
a=int(s)
print(a)
sum=0
total=0
for i in s:
    sum+=int(i)
    print(sum) 
    