"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Přemysl Ježek
email: j.prema@seznam.cz
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
garpike and stingray are also present.''',
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
# Seznam registrovanych uzivatelu
REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# Zadani prihlasovacich udaju
user_name = input("username: ")
password = input("password: ")

# Overeni uzivatele a hesla
if REGISTERED_USERS.get(user_name) == password:
    print("-"*40)
    print("Welcome to the app,",user_name )
    print("We have 3 texts to be analyzed.")
    print("-"*40)

   
    # Vyber textu k analyze
    selection_of_text = input("Enter a number btw. 1 and {} to select: ".format(len(TEXTS)))
    print("-"*40)

    # Kontrola spravneho vstupu
    if not selection_of_text.isdigit():
        print("Wrong input. enter number!!!")
        exit()
    elif not (1 <= int(selection_of_text) <= len(TEXTS)):
        print("the number is not in the required range!!!")
        exit()


    # Vybrany text
    vyber_textu = TEXTS[int(selection_of_text)-1]
        
    # Rozdeleni textu na slova
    words =vyber_textu.split()
    words_count = len(words)

    # Ocisteni slov od tecek a carek
    cleaned_words = []                                         
    for word in words:                                         
        cleaned_word = word.replace(",", "").replace(".", "")   
        cleaned_words.append(cleaned_word)                     

    # Pocet slov podle ruznych kriterii
    titlecase_words = 0
    uppercace_words = 0
    lowercase_words= 0
    numeric_strings = 0
    sum_numbers = 0
    for word in cleaned_words:
        if word.istitle():
            titlecase_words += 1
        if word.isupper() and word.isalpha():
            uppercace_words += 1
        if word.islower():
            lowercase_words += 1
        if word.isdigit():
            numeric_strings+= 1
        if word.isdigit():
            sum_numbers+=int(word)

    # Vypis vysledku
    print("There are", words_count, "words in the selected text.")
    print("There are",titlecase_words,"titlecase words.")
    print("There are",uppercace_words, "uppercase words.")
    print("There are",lowercase_words,"lowercase words.")
    print("There are",numeric_strings,"numeric strings.")
    print("The sum of all the numbers ",sum_numbers)


     # Analyza delky slov a vykteslení sloupcového grafu
    number_of_words = []
    for word in cleaned_words: 
        number_of_words.append(len(word))

    max_len = max(number_of_words)
    max_count = max(number_of_words.count(i) for i in number_of_words) 
   # bar_width = max_count

    
    print("-" * 40)
    print(f"{'LEN':>3} | {'OCCURRENCES'.ljust(max_count)} | {'NR.':>3}")
    print("-" * 40)

    for i in range(1, max_len + 1):
        count = number_of_words.count(i)  
        if count > 0:  
            print(f"{i:>3} | {'*' * count:<{max_count}} | {count:>3}")
    
else:   
    print("\n","unregistered user, terminating the program.")
    exit()

    
    

