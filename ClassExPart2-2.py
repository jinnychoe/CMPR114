#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Challenge 2: Loop that multiplies

product = 0 #initializes product

while (product < 100): #loops as long as product is < 100
    num = float(input("Enter a number: ")) #requests user input
    product = num * 10 #multiplies input by 10 and assigns to product
    print ("Product is :",product)
    
print ("End loop")
