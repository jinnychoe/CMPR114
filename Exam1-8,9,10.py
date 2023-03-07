#Jinny Choe
#Quiz 1
#Project 6

#initializes var
score = 0
avg = 0
totalscore = 0
getscore = True

while getscore == True:

    for i in range(4):
        score = float(input(f"Input score #{i+1}: ")) #user inputs 
        totalscore += score
        
    avg = totalscore/4 #calculates average score
    print (f"The average is {avg:.2f}") #prints results
     
    if avg > 100:
        print ("Please input the scores again. The average is greater than 100. ") #user inputs scores again
        totalscore = 0
        i = 0
    elif avg >=90 and avg <=100: #defines letter grade
        getscore = False  #user does not input scores again
        print ("The grade is A.") #prints results
    elif avg >=80 and avg <=89:
        getscore = False 
        print ("The grade is B.") 
    elif avg >=70 and avg <=79:
        getscore = False 
        print ("The grade is C.") 
    elif avg >=60 and avg <=69:
        getscore = False 
        print ("The grade is D.") 
    elif avg < 60: 
        getscore = False 
        print ("The grade is F.") 

