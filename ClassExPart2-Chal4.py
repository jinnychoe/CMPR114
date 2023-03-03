

#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Challenge 4: Calories burned

minlist = [10,15,20,25,30] #list of minutes
callist = [] #initializes calories burned per minute list
calpermin = 4.2 #sets calories per minute burned multiplier

#print results
print ("Minutes exercised\tCalories burned")
for n in range(len(minlist)): #loops through each item in minutes list
    callist.append(calpermin*minlist[n]) #adds calories burned per minute to calorie list
    print(f"{minlist[n]}\t\t\t{callist[n]:.1f}") # prints minutes and calorie list
