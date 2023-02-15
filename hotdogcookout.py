#Jinny Choe
#2/13/2023
#Homework week 2 Project #2: Hot Dog Cookout

import math

#asks user for number of total guests attending
guests = int(input('How many people will attend the cookout? '))

#asks user for number of hot dogs eaten per guests
hdperguest = int(input('How many hot dogs will each guest have? '))

#calculates total number of hot dogs needed
totalhd = guests * hdperguest

#calculates packages of hotdogs needed
packagehd = math.ceil(totalhd/10)

#calculates packages of buns needed
packagebun = math.ceil(totalhd/8)

#calculates number of hotdogs left over
leftoverhd = packagehd*10 - totalhd

#calculates number of buns left over
leftoverbun = packagebun*8 - totalhd

print("Minimum number of hot dog packages required: " + str(packagehd))
print("Minimum number of bun packages required: " + str(packagebun))
print("Left over hot dogs: "+ str(leftoverhd))
print("Left over buns: "+ str(leftoverbun))
