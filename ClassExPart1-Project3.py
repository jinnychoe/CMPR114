#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 1 Project 3

#Named constant, a named constant is a variable that does not change.
MAX_TEMP = 102.5

#Get the substance's temperature
temperature = float(input("Enter the temperature for today: "))

#As long as necessary, instruct the user to adjust the thermostat
while temperature > MAX_TEMP:
    print('The temperature is too high.')
    temperature = float(input('Enter the new Celsius temperature: '))
    
#remind user to check temp again in 15 min
    print('The temperature is acceptable.')

