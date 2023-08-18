"""
projekt_1.py: druhy projekt do Engeto Online Python Akademie - Bulls & Cows
author: Pavla Svabenska
email: pavla.svabenska@seznam.com
discord: Pavla S#1531
"""
import random

#generate random number, range 1000 - 9999, no duplicates in digits

def random_number():
    while True:
        number = random.randint(1000, 9999)
        number_str = str(number)
        if len(set(number_str)) == 4:
            return number_str
        
secret_number = random_number()

     
# check if the number is valid: integer, 4digits, not starting with 0 and no duplicate numbers

def valid_number(num):
    try: 
        #integer
        num = int(num)

        # 4 digits and duplicates and numbers starting with 0 conditon
        if 1000 <= num <= 9999:         
            num_str = str(num)
            if len(set(num_str)) == 4 and num_str[0] != "0" and len(num_str) == len(set(num_str)):
                return True
            
        return False
    
    except  ValueError:
        return False

lines = 48 * "-"
print("Hi there!\n" + 
        lines +
        "\nI've generated a random 4 digit number for you.\n" +
        "Let's play a bulls and cows game.\n")

attempts = 0


while True:
    attempts += 1
    bulls = 0
    cows = 0

    guess = input("Enter a number: \n" + lines + "\n>>>")
    

    if not valid_number(guess):
        print("Invalid input. Please enter a valid 4 digits number.")
        continue

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    
    #grammar check bull vs bulls, cow vs cows
    if bulls == 1:
        bulls_text = "1 bull"
    else:
        bulls_text = f"{bulls} bulls"

    if cows == 1:
        cows_text = "1 cow"
    else:
        cows_text = f"{cows} cows"

    print(f"{bulls_text}, {cows_text}")
    print(lines)


    # attempts scale
    if bulls == 4:
        if attempts == 1:
            message = "amazing"
        elif attempts in range(2,8):
            message = "good"
        elif attempts in range(8,11):
            message = "average"
        else:
            message = "not so good"
            
        print(f"Correct, you've guessed the right number in {attempts} guesses! That is {message}.")
        break




