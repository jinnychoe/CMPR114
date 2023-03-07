#Jinny Choe
#Quiz 1
#Project 4

#initializes var
sales = 0

#user inputs 
for i in range(3):

    sales = float(input("Enter the sales: "))
    commission = 0
    #determines the commission based on the commission table
    if sales >= 50000 and sales < 70000:
        commission = 10
    elif sales >= 70000 and sales < 90000:
        commission = 20
    elif sales >= 90000 and sales <= 100000:
        commission = 30
    print (f"The commission is {commission}%") #prints results
