#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 1 Challenge 2: Sales Commision

#Initialize variables
TotalSales = 0
TotalCom = 0 
n = 1


while (n < 5):
  
    sales = float (input ("Enter the amount of sales: " )) #user input sales
    comm_rate = float(input("Enter the commission rate in decimal: ")) #user input commission rate
    comm = sales * comm_rate #calculates commission on sale
    TotalCom = TotalCom + comm #adds commission to total commission
    TotalSales = TotalSales + sales #adds sale to total sales
    n += 1 #adds iteration number to loop
      
#prints results
print (f"Total Sales:  {TotalSales:.2f}")
print (f"Total Commission:  {TotalCom:.2f}")
