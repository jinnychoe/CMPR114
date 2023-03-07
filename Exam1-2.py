#Jinny Choe
#Quiz 1
#Project 2

#initializes var
i=0
sumtotal = 0
avg = 0

#user inputs scores
for i in range(4):
    score = float (input("Enter score: "))
    sumtotal += score
    
#calculates avg
avg=sumtotal/4

#prints results
print (f"Expeced outcome is: sum = {sumtotal:.0f}, average = {avg:.0f}")