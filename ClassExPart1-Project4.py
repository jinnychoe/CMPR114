#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 1 Project 4

#program is infinite loop
#var controls loop

keep_going = 'y'

while keep_going == 'y':
# get a sales persons sales & comm rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    
    #calculate commission
    commission = sales * comm_rate
    
    print (f"The commission is ${commission:,.2f}")
