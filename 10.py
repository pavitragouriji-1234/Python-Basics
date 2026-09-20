#For Loop PROBLEMS
for i in range (3,11):
    for j in range (1,11):
        print(f"{i}x{j}={i*j}")


for i in range(3,31,3):
    print(i)


sum=0
for i in range(1,11):
    sum+=i
print(sum)



s="PAVITRA"
for letter in s:
    print(letter)



vowels="AEIOU"
count=0
for i in vowels:
    count+=1
print(count)
    


numbers = [2, 5, 8, 11, 14, 17, 20]
count=0
for i in numbers:
    if i%2==0:
        count+=1
print(count)



numbers = [10, 25, 7, 40, 18]
max=0
for i in numbers:
    if i>max:
        max=i
print(max)



word = "PYTHON"
reverse=0
for i in word[::-1]:
    print(i)


word = "banana"
count=0
for i in word:
    if i=="a":
       count+=1
print(count)


for i in range(2,6):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")


#PRINT  PRIME NUMBERS
for n in range(2,51):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(n)


#nested loop
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
