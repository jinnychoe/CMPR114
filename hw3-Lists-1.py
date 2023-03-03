#Jinny Choe
#3/1/2023
#Week 3 Homework List Question #1

#The get_scores function gets a series of test scores from the user and stores them in a list.
#A reference to the list is returned
def get_scores():
    
    #Create an empty list.
    test_scores = []
    
    #Create a variable to control loop
    again = 'y'
    
    #Get the scores from the user and add them to the list
    while again == 'y':
        #Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)
        
        #Want to do this again?
        print ('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()
    
    #return the list.
    return test_scores
#The get_total function accepts a list as an arguement and returns the total of the values in the list

def get_total(value_list):
    #create a variable to use as an accumulator
    total = 0.0
    
    #calculate the total of the list elements.
    for num in value_list:
        total += num
    
    #return total
    return total

def main ():

    scores = get_scores() #uses get_score function to call scores

    totalscores = get_total(scores) #sums scores

    avgscore = totalscores/len(scores) #calculates average scores
    
    #prints results
    print('Scores: ',scores)
    print('Total scores: ',totalscores)
    print('Average: ',avgscore)
    
    #output to file
    
    scorefile = open("scorefile.txt", 'w')
    scorefile.write('Scores: ' + str(scores) + '\n')
    scorefile.write('Total: ' + str(totalscores) + '\n')
    scorefile.write('Average: ' + str(avgscore) + '\n') 
    scorefile.close()

#call the main function
if __name__ == '__main__':
    main()