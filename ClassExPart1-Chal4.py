#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 1 Challenge 4: Looping Strings

firstname = "Jinny" #defines my name
lastname = "Choe"

print ("First name:",firstname) #prints my name
print("Last name:",lastname)

names = ['Winken', 'Blinken', 'Nod'] #defines list

print ("List:", names) #prints list

if lastname in names: #finds my name in list
    print ("Last name Choe was found on list.")
else:
    print ("Last name Choe was not found on list.")

names.append(lastname) #appends name to list

print ("New list:",names) #prints new list

for name in names[:]: #removes names that are not same as Choe
    if name != lastname:
        names.remove(name)
    elif name == lastname:
        print ("New list:", names)
        print ("Your full name is", firstname, lastname)


