#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 2 Project 3

#calculate retail price

MARK_UP = 2.5 #The markup percentage
another = 'y' #var to control loo

#process one or more items
while another == 'y' or another == 'Y':
#get wholesale cost
    wholesale = float(input("Enter the item's wholesale cost: "))
    
    #calculate retail price
    retail = wholesale * MARK_UP
    
    #validate entry
    while wholesale < 0:
        print ('cannot be negative number, try again')
        wholesale = float(input('enter the correct wholesale cost: '))
    
    #display retail price
    print(f'Retail price: ${retail:,.2f}')
    
    #another input
    another = input ('Do you have another item? (Enter y for yes) ')
    
    
