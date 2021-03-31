# Program is asking your name. If input data is blank loop while will run
while True:
    print('Please, enter your name')
    name = input()
    while name == '': # When I put False rather than, loop doesn't work. Could you explain? Does it mean, taht '' is False value for strings?
        print('No input data. Please put your name')
        name = input()

    print('The attepmt was passed. Hello ' + name)

#if the variable is equal to the value entered, logically user entered something
#elif name == name:
#        print('Hello ' + name)    

#Section 'Enter your age'   

    print('Enter your age, please')
    age = input()
    while age == '':
        print('You have not entered any data. Enter your age, please?')
        age = input()

    print('Thank you' + name + 'Then you have ' + str(age) + 'years old.')

#variable current date
    current_year = int(2021)

#display the year you were born
    day_birth = current_year - int(age)
    print(name + ' You born in ' + str(day_birth))

#Variable that marks the date when World War II broke out
    war = 1939
    print(name + ' you born ' + str(day_birth - war) + ' years after the outbreak of the Second World War')

#A condition that checks when the user was born. Whether before 2000 or after 2000.
    if current_year - int(age) < 2000:
        print(name + ' in 2000 year you have' + str(int(age) - 21) + ' years old.')

#If the user was born after 2000, the following condition will be met
    else:
        print(name + ' You have not been in the world yet!!')

#Declaration of a variable of the XXII century
    century_XXII = 2101
    year_in_XXII_century = century_XXII - day_birth

    print(name + ' in XXII century you will have ' + str(year_in_XXII_century) + ' years old')

#Condition with the answer 'yes or no'
    if input('Do you want to repeat(y/n)') == 'n':
        break   