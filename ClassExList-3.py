#Jinny Choe
#2/27/2023
#Class Exercise Week 3.7 Lists Question 3: Insert and Remove

#this program will add to the list and delete from the list
def main():
    names = ['Howard', 'Jamie','Jill']
    
    print ('The list before the insert or remove:')
    print(names)
    
    NamesRemove = input('Enter the name to remove: ')
    
    names.insert(0,'Joe')#inserts the new name at element 0, moving or shifting element 0 to 1
    names.remove(NamesRemove)#removes the name from the list
    print ('The list after the insert:')
    print(names)
    
main()

def total():
    numbers =[1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum +=value #total the numbers in the list
    average = sum/len(numbers) #len fxn returns number of items in list
    print('The total is ', sum, '. The average is ', average,'.')

total()