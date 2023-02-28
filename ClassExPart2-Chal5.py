#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Challenge 5: Lap Times

totallapnum = int(input("Enter the number of laps: ")) #requests user input total number of laps ran
laptime = [] #initializes list and other var
avglaptime = 0 
fastestlaptime = 0
slowestlaptime = 0
time = 0
totallaptime = 0

for lapnum in range(totallapnum): #creates loop to ask user for laptime
    time = float(input(f"Enter time for lap {lapnum+1}: ")) #user input lap time for each lap ran
    laptime.append(time) #adds lap time to list
    totallaptime =+ time #adds lap time to total lap time
    
avglaptime = totallaptime/lapnum #calculates average lap time
fastestlaptime = min(laptime) #determines slowest lap time
slowestlaptime = max(laptime) #determines fastest lap time

#print results
print ("Average lap time: ", avglaptime)
print ("Slowest lap time: ", slowestlaptime)
print ("Fastest lap time: ", fastestlaptime)
