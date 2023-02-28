#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Question 4

minlist = [10,15,20,25,30]
callist = []
calpermin = 4.2
print ("Minutes exercised      Calories burned")
for n in range(len(minlist)):
    callist.append(calpermin*minlist[n])
    print(f"{minlist[n]}                     {callist[n]:.1f}")
