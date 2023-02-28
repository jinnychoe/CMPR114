#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 1 Question 1

#Initialize temperature sum and average
TempSum = 0
TempAvg = 0
Temp = 0
n = 0

MaxTemp = 102.5

while (n < 4):
  
    Temp = float (input ("Enter the temperature " + str(n+1) + ": "))
   
    if (Temp >= MaxTemp): #if temp is too high, rejects temp
        print ("Your temperature is too high.")
    else:
        n += 1 #adds iteration number to loop
        TempSum = TempSum + Temp #Adds temp to sum of temps

TempAvg = TempSum / n #Calculates Average Temp
print ("Sum of temperatures: ", TempSum)
print ("Average of temperatures: ", TempAvg)
