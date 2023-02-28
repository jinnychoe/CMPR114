#Jinny Choe
#2/27/2023
#Class Exercise Week 3.7 Lists Question 1

#creating Lists
evenNumbers = [2,4,5,8,10]
print (evenNumbers)

names = ["ian","jason","molly"]
print (names)

info =["ally", 27, 1550.87]
print (info)

numbers = [5] * 5
print (numbers)

#using a for loop to print numbers in a Lists
LoopNumbers = [1,2,3,4,5,6,7]
for n in LoopNumbers:
    print (n)
    
#using a while loop and incrementing by 1
index = 0 
while index < 4:
    print (LoopNumbers[index])
    index+=1 

#the len function counts how many numbers there are in the Lists
size = len(LoopNumbers)
print (size)

#creating Lists
evenNumbers =[2,4,6,8,10]
print (evenNumbers[0])

#creating Lists
sum = 0 
evenNumbers = [2,4,6,8,10]
for a in evenNumbers:
    sum+=a#adds the numbers in the Lists
print (evenNumbers[0])
print ("total sum " + str(sum))
