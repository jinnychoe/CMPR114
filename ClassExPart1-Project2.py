#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 1 Project 2 

#Create a variable to control the loop
keep_going = 'y'

#calculate series of commissions
while keep_going == 'y':
#get sales person's sales & commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
#calculate comission
    commission = sales * comm_rate
#display the commission
    print ('The commission is $', format(commission, ',.2f'))
#asks user to continue
    keep_going = input('Do you want to calculate another '+'comission (Enter (y for yes): ')

