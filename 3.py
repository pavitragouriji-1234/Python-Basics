L=["10","20","30","40","50"]
print(int(L[0]),int(L[1]),int(L[2]),int(L[3]),int(L[4]))
sum=0
for i in range(len(L)):
    sum+=int(L[i])
    print("sum is:",sum)

#____________________________________________________________________________________________________

s="10"
print(int(s))
if int(s)%2==0:
    print("it is even number")
else:
    print("it is odd number")

#_________________________________________________________________________________________________________

a="1.2,3.5"
print(float(a.split(",")[0])+float(a.split(",")[1]))
average=0
for i in a.split(","):
    average+=float(i)
average/=len(a.split(","))
print("average is :",average)