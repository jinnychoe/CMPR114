#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Question 3:
n=0 #initializes count for the day
totalbugs = 0
days = 5 #total number of days

for n in range(days): #loops for 5 days
    dailybugs = int(input(f"How many bugs did you collect on day {n+1}: ")) #user input for daily bugs counted
    totalbugs = totalbugs + dailybugs #adds daily bugs counted to total bug count

print ("Total bugs collected over",days, "days:", totalbugs, "bugs")
    