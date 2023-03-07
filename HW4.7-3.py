#Jinny Choe
#3/6/2023
#Week 4, Homework Ch 7, Question 3

test_tup = ([17,28],[93,11],[20,17])

#initializes var
total=0


for i in test_tup: #goes through each element
    total += sum(i) #sums all the values in the list

print(f"The total of all values in the tuple is {total}") #prints result