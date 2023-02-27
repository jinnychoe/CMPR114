#Jinny Choe
#2/27/2023
#Homework 3 Project 1: Distance Traveled
speed = int (input ("What is the speed of the vehicle in mph? "))
hours = int(input ("How many hours has it traveled? "))
print ("Hour       Distance traveled")
n = 1 #starts at first hour
while(n <= hours): 
    distance = n * speed #calculates distance traveled
    print (n, "       ", distance)
    n = n + 1 #adds another hour
    
