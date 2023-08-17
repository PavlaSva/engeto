"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Svabenska
email: pavla.svabenska@seznam.com
discord: Pavla S#1531
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users_pwd = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = input("Enter your username:").lower()
password = str(input("Enter the password:"))

if users_pwd.get(username) == password:
    print(f"welcome to the app, {username}. We have 3 texts to analyze")
else:
    print("unregistered user, terminating the program...")
    quit()


user_input_str = input("Enter a number between 1 and 3 to select: ")

if user_input_str.isdigit() and 1 <= int(user_input_str) <= 3:
    print("The program will analyze text number", user_input_str)
else:
    print("Invalid input. Please enter an integer between 1 and 3. Terminating the program.")
    quit()
    
user_input = int(user_input_str)


# number of words
words = TEXTS[user_input - 1].split()
length = len(words)

# number of words, title case
titlecase_words = 0
for word in words:
    if word[0].isupper():
        titlecase_words +=1


#number of words, capital letters
uppercase_words = 0

for word in words:
    if word[:-1].isupper():
        uppercase_words +=1


# numbers of words, lowercase letters
lowercase_words = 0

for word in words:
    if word.islower():
        lowercase_words +=1


#number of digits

number_of_digits = 0

for word in words:
    if word.isnumeric():
        number_of_digits +=1

# sum of all digits
sum_digits = 0

for word in words:
    if word.isnumeric():
        sum_digits += int(word)
  
# Calculate the length of each word
word_lengths = []

for word in words:
    word_lengths.append(len(word))
    word_lengths.sort()

# Calculate the frequency of each word length
frequency = {}

for word_freq in word_lengths:
    if word_freq in frequency:
        frequency[word_freq] += 1
    else:
        frequency[word_freq] = 1



print(f"There are {length} words in the selected text.")
print(f"There are {titlecase_words} titlecase word.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {number_of_digits} numeric strings.")
print(f"The sum of all the numbers {sum_digits}.")

print("---------------------------")
print("LEN|\tOCCURENCIES\t|NR.")
print("---------------------------")
for word_freq, freq in frequency.items():
    print(word_freq, "|", "\t", freq * "*" , "\t|", freq)




