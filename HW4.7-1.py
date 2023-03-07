#Jinny Choe
#3/6/2023
#Week 4, Homework Ch 7, Question 1


test_tup = (15,20,123,47,26,81) #defines variables
sum=0
num=0
i=0

while (i < len(test_tup)): #starts loop to add all items in tuple
    num = test_tup[i-1] #get item from tuple
    sum += num #adds item to sum total
    i+=1 #adds to iteration counter
    
print (f"The sum of the test tuple is {sum}") #prints result
