#Jinny Choe
#Quiz 1
#Project 5

#initializes var
sales = 0
salary = 0

#user inputs 
for i in range(3):

    sales = float(input("Enter the sales: "))
    commission = 0
    #determines the commission based on the commission table
    if sales >= 50000 and sales < 70000:
        commission = 10
        salary = 70000
    elif sales >= 70000 and sales < 90000:
        commission = 20
        salary = 80000
    elif sales >= 90000 and sales <= 100000:
        commission = 30
        salary = 90000
    totalcommission = (sales * (commission / 100))
    totalsalary = (salary + totalcommission)
    print (f"The commission is {commission}%") 
    print (f"The total salary is ${totalsalary:.2f}")



