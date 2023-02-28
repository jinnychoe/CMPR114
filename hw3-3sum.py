#Jinny Choe
#2/27/2023
#Homework 3 Project 3: Sum of Numbers

#sets input number to zero and sum to zero
n = 0
sum = 0

while (n >= 0):
    n = float(input("Input a positive number. (Or input a negative number to exit)"))#User input number 
    if (n >= 0):
        sum = sum + n #adds positive number to total

#prints total 
print ("Sum of all positive numbers entered: ", {sum})
