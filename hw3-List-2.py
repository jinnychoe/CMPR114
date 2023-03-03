#Jinny Choe
#3/2/2023
#Week 3 Homework List Question #2

#initializes variables
totalnumbers=0
totalsumnumbers=0
avg=0
numlist = []
numindex = 0
maxnum = 0
minnum = 0


print ("Enter 20 numbers.")
while numindex < 20:
    num = float(input(f"Enter #{numindex + 1}: " )) #user input for 20 numbers
    totalnumbers += num #adds number to total sum
    numlist.append(num) #adds number to list
    numindex+=1 #adds count to loop iteration

maxnum = max(numlist) #calculates maximum number
minnum = min(numlist) #calculates minimum number
avg = totalnumbers/20 #calculates average number

print (f"The smallest number on the list is {minnum}.")
print (f"The largest number on the list is {maxnum}.")
print (f"The total sum of all numbers on the list is {totalnumbers}.")
print (f"The average of all numbers on the list is {avg}.")
