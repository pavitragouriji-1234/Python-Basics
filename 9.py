#basic counting with while loop
count=0
while count<=10:
    print(count)
    count+=1

#odd numbers printer
i=0
while i<=20:
    if i%2!=0:
        print(i)
    i+=1


#ticket booking simulation
seats=8
while seats>0:
    print("seats are booked")
    seats-=1
    print("seats remaining:",seats)
print("seats are not available")



#countdown timer
countdown=10
while countdown>=1:
    print(countdown)
    countdown-=1
print("Happy New Year")
