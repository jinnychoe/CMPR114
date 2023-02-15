#Jinny Choe
#2/13/2023
#Homework week 2 Project #3: Software Sales

#retail price
retail  = 99

#User inputs number of packages purchased
quantity = int(input('Input the number of packages: '))

#determines discount value based on quantity purchased
if quantity < 10:
    discount = 0 
elif quantity >= 10 and quantity <=19:
    discount = 10
elif quantity >=20 and quantity <= 49:
    discount = 20
elif quantity >= 50 and quantity <= 99:
    discount = 30
elif quantity >= 100:
    discount = 40

#calculates amount discount based on quantity purchased
amountdiscount = (discount/100)*(quantity*retail)

#calculates total after discount
total = (quantity * retail) - amountdiscount

print ('Discount: '+str(discount)+'%')
print ('Total after discount: $'+str(total))

