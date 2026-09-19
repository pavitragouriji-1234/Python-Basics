T1=(1,2,3,4,5)
print(T1)
print(T1[2:5])
T2=(7,8,9,10)
print(T1+T2)
#_____________________________________________________________________________________________________________
S1={"apple","banana","grapes"}
S2={"mango","apple","cherry"}
print(S1&S2)
print(S1|S2)
print(S1-S2)
print(S1.add("mango"))
print(S1.remove("apple"))
print(S1.discard("mango"))
#____________________________________________________________________________________________________
L=[1,2,3,4,5]
t=tuple(L)
print(t)
s=set(L)
print(s)
t=t+(10,)
s.add(12)
print(t)
print(s)


