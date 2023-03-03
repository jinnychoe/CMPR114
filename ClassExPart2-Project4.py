#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 2 Project 4

#displays property taxes
TAX_FACTOR = 0.0065 #tax factor

#lot number
print('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))

#continue loop as long as lot isn't 0
while lot != 0:
    value = float(input('Enter the property value: '))
    
    #calculate the property tax
    tax = value * TAX_FACTOR
    
    #print tax
    print(f'Property tax: ${tax:,.2f}')

    #get next lot number
    print('Enter the property lot number or enter 0 to end.')
    lot = int(input('Lot number: '))
    
