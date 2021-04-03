#Global Variables
user_name = ''
user_age = ''

#Function greetings
def greeting():
    print('Welcome to the second version program.')

#Function is asking user about name and surname. Data entry controls implemented
def name_and_surname(userName):
    print('Please, enter your name and surname')
    userName = input()
    
    while userName == '':
        print("No enter data! What is your name?")
        userName = input()
    
    global user_name
    user_name = userName
     
    return print('Hello ' + userName + ' !')

#Function is asking user about his age. Data entry controls implemented
def user_name_age(userNameAge):
    print(user_name + ',' + ' how old are you?')
    userNameAge = input()
    while userNameAge == '':
        print("You don't enter any data. Please write, how old are you?")
        userNameAge = input()

    global user_age
    user_age = userNameAge

    return print("Programs gives some interesting facts about your age.")

#Interesting facts related to user_name age
def interesting_facts(day_birth):
    current_year = int(2021)
    war = 1939
    day_birth = current_year - int(user_age)
    century_XXII = 2101
    year_in_XXII_century = century_XXII - day_birth

    print('You born in ' + str(day_birth) + ' year.')
    print(user_name + ' you born ' + str(day_birth - war) + ' years after the outbreak of the Second World War')
    
    #A condition that checks when the user was born. Whether before 2000 or after 2000.
    if current_year - int(user_age) < 2000:
        print(user_name + ' in 2000 year you have ' + str(int(user_age) - 21) + ' years old.')
    #If the user was born after 2000, the following condition will be met
    else:
        print(user_name + ' You have not been in the world yet!!')

    #Declaration of a variable of the XXII century
    print(user_name + ' in XXII century you will have ' + str(year_in_XXII_century) + ' years old')

    #How many characters have your name and surname
    print ('Your name have ' + str(int(len(user_name))) + ' characters.')

greeting()

def main():
    name_and_surname(user_name)
    user_name_age(user_age)
    interesting_facts(user_age)
while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break