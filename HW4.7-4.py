#Jinny Choe
#3/6/2023
#Week 4, Homework Ch 7, Question 4

input_tup = ([2,20],[44,1],[3,13])

#intializes var
new_list = []
sorted_newlist =[]

for i in input_tup: #goes through each list in the tuple
    total = sum(i) #sums up total in lists
    sublist = list(i) #creates a list from items in tuple list
    print (sublist)
    sublist.append(total) #adds total to list
    print(sublist)
    new_list.append(sublist) #creates item of list in new list
    print(new_list)
    
sorted_newlist = sorted(new_list,key=lambda x: x[2]) #sorts the new list by the 3rd index in nested list

for x in sorted_newlist:
    del x[2] #deletes the 3rd index in the nested list 
    
sorted_tup = tuple(sorted_newlist) #creates tuple 


print(f"The tuple is sorted by list total: {sorted_tup}")
