#Jinny Choe
#2/27/2023
#Class Exercise Week 3.7 Lists Question 4: Output file
    

def total():
    numbers =[1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum +=value #total the numbers in the list
    average = sum/len(numbers) #len fxn returns number of items in list
    print('The total is ', sum, '. The average is ', average,'.')

    #writes numbers list to file
    outfile = open('total.txt','w') 
    outfile.write(str(numbers))
    outfile.close()
    print('Recorded numbers in the list')
total()
