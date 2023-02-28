#Jinny Choe
#2/27/2023
#Homework 3 Project 2: Average rainfall

#User input number of years
years = int(input("Enter the total number of years: "))

#Sets total rainfall and total month count to zero
totalrainfall = 0
totalmonths = 0


for year in range(years): #outerloop for year
   
    for month in range(12):  #innerloop for each month of the year
   
        rainfall = float(input(f"Enter the inches of rainfall for month {month+1} of year {year+1}:  ")) #User input of rain for year & month
     
        totalrainfall += rainfall #adds rainfall input in total rainfall
        
        totalmonths += 1 #adds a month to the month count

#calculate the average rainfall per month
avgrainfall = totalrainfall/totalmonths

#prints total months, total rainfall, average rainfall
print(f"Total number of months: {totalmonths}")
print(f"Total inches rainfall: {totalrainfall}")
print(f"Average inches of rainfall each month: {avgrainfall}")
