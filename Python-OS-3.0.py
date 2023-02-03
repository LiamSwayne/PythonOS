#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Python OS 3.0 created by Liam Swayne

#imports
import time
import random
import ast

#os vars
user_input = ''
shut_down = False
app_select2 = False
app_select = '''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ Select an app:         ▓
▓                        ▓
▓ - Wheel of Fortune     ▓
▓ - Gallery              ▓
▓ - Calculator           ▓
▓                        ▓
▓ Type 'exit' to system  ▓
▓ shutdown.              ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'''

#get and convert data type function
def getType(input):
    input = str(input)
    if input == "True":
        input = True
    elif input == "False":
        input = False
    else:
        try:
            input = float(input)
            if str(input).endswith(".0"):
                input = int(input)
        except ValueError:
            pass
    return input

#input function
def take_input():
    a = input()
    a = a.upper()
    a = getType(a)
    return a

#gallery app
def gallery():
    slide_number = 0
    slides = ['''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓   ╔═ ▄▄▄ ││ ╔╗ █/ \/   ▓
▓   ║╗ █▄█ ││ ╠╝ █  /    ▓
▓   ╚╝ █ █ ││ ╚═ █ /     ▓
▓ Press enter to visit   ▓
▓ next slide, or '-' and ▓
▓ enter to visit         ▓
▓ previous slide.        ▓
▓                        ▓
▓ 'e' to exit.           ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''']
    user_input = ""
    while(user_input != 'e'):
        print(slides[slide_number])
        decision = False
        while decision == False:
            user_input = take_input()
            if user_input == '\n':
                slide_number += 1
                decision = True
                if slide_number == len(slides):
                    slide_number = 0
            elif user_input == '-\n':
                decision = True
                slide_number -= 1
                if slide_number < 0:
                    slide_number = len(slides)-1
            elif user_input == 'e':
                decision = True
            else:
                print("Invalid input.")

#calculator app
def calculator():
    user_input = input("Enter a mathematical expression: ")
    while(user_input != 'e' and user_input != 'E'):
        try:
            print(eval(user_input))
        except:
            ValueError
        user_input = input("Expression: ")

#wheel of fortune app
def wheel_of_fortune():
    #variables for wheel of FORTUNE!
    expressions = ["CASE IN POINT","ONCE IN A BLUE MOON","GO FOR GOLD","MAKE OR BREAK","RAINING CATS AND DOGS","CAT'S OUT OF THE BAG","PAST THE POST","TIP THE SCALES","SETTLE A SCORE","TWISTS AND TURNS"]
    line = random.choice(expressions)
    cash_won = 0
    letter_check = False
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letters_taken = []
    vowels = ["A","E","I","O","U"]
    line_dots = line
    for i in range(len(line_dots)):
        if line_dots[i] in alphabet:
            line_dots = line_dots[:i]+"*"+line_dots[i+1:]
    letter_guess = ""
    first_letter = True
    second_letter = False
    new_cash = 0
    host_line = ""
    prize_door = 0
    user_input = ""
    door_choice = 0
    show_door = [1,2,3]
    show_door_2 = 0
    choice = ""
    final_door = 0
    index = 0
    host_compliments = ["▓ Host: Fantastic!       ▓","▓ Host: Spectacular!     ▓","▓ Host: Incredible!      ▓","▓ Host: Magnificent!     ▓","▓ Host: Extraordinary!   ▓"]
    yes_no = False
    yes_no_input = ""
    correct_guess = False
    
    print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓  ║║║║║╔═╔═║   ╔═╗╔═    ▓
▓  ║║║╠╣╠═╠═║   ║ ║╠═    ▓
▓  ╚╩╝║║╚═╚═╚═  ╚═╝║     ▓
▓                        ▓
▓  ╔═╔═╗╔╗═╦═║ ║╔╗ ║╔═   ▓
▓  ╠═║ ║╠╩╗║ ║ ║║╚╗║╠═   ▓
▓  ║ ╚═╝║ ║║ ╚═╝║ ╚╝╚═   ▓
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
    time.sleep(1.5)
    print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░▒░░░▒░░░░░░░░░▓
▓░░░░░░░░░░░░░░▒░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░░░░░▒░░░░░░░░░▓
▓░░░░░░░░░░▒░░░▒░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
    time.sleep(1)
    print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░▒░░░▒░░░░░░░░░▓
▓░░░░░░░░░░░░░░▒░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░▒░░░░░░░░░░░░░▓
▓░░░░░░░░░░▒░░░░░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
    time.sleep(1)
    print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒░░░░░░░░░░▓
▓░░░░░░░░░░▒░░▒░░░░░░░░░░▓
▓░░░░░░░░░░░░░▒░░░░░░░░░░▓
▓░░░░░░░░░░░░░▒░░░░░░░░░░▓
▓░░░░░░░░░░░░░▒░░░░░░░░░░▓
▓░░░░░░░░░░░░░▒░░░░░░░░░░▓
▓░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░▓
▓░░░░░░░░░░░░░░░░░░░░░░░░▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
    time.sleep(1)

    while line != line_dots:
        new_cash = 0
        letter_check = False
        if first_letter == True:
            print("Guess a letter (the first guess is blind):")
            first_letter = False
            second_letter = True
        elif second_letter == True:
            print("Guess a letter (remember you can always type the phrase):")
            second_letter = False
        else:
            print("Guess a letter:")
        while letter_check == False:
            letter_guess = take_input()
            if len(letter_guess) == 1:
                if letter_guess in alphabet and letter_guess not in letters_taken:
                    letter_check = True
                    letters_taken.append(letter_guess)
                else:
                    if letter_guess in letters_taken:
                        print("That letter's already been guessed.")
                    else:
                        print("That's not a letter.")
            elif len(letter_guess) == 0:
                print("You gotta type something.")
            else:
                print("Is that your guess at the phrase? (y/n)")
                yes_no = False
                while yes_no == False:
                    yes_no_input = take_input()
                    if yes_no_input == "Y" or yes_no_input == "YES":
                        yes_no = True
                        letter_check = True
                        if letter_guess == line:
                            correct_guess = True
                        else:
                            correct_guess = False
                    elif yes_no_input == "N" or yes_no_input == "NO":
                        yes_no = True
                        print("Guess a letter:")
                    else:
                        print("Invalid input.")
        if line.count(letter_guess) == 0 and len(letter_guess) == 1:
            cash_won -= 100
        if letter_guess in alphabet:
            for i in range(len(line)):
                if line[i] == letter_guess:
                    line_dots = str(line_dots)[:i]+letter_guess+str(line_dots)[i+1:]
        if letter_guess in vowels:
            new_cash = line.count(letter_guess)*100
            cash_won -= new_cash
        elif letter_guess in alphabet:
            new_cash = line.count(letter_guess)*200
            cash_won += new_cash
        elif correct_guess == True:
            new_cash = line_dots.count("*")*200
            cash_won += new_cash
            line_dots = line
        elif correct_guess == False:
            cash_won -= 100
        string_line = ("▓ "+line_dots+"                                   ")[:25]+"▓"
        cash_line = (str(cash_won)+"                       ")[:12]+"▓"
        if len(letter_guess) > 1:
            if correct_guess == True:
                host_line = "▓ Host: That's the       ▓\n▓ phrase! You got it!    ▓"
            else:
                host_line = "▓ Host: That is not the  ▓\n▓ phrase.                ▓"
        elif new_cash == 0:
            host_line = "▓ Host: No hits! Take    ▓\n▓ another crack at it.   ▓"
        elif letter_guess in vowels and new_cash > 0:
            host_line = "▓ Host: A vowel, that's  ▓\n▓ gonna cost you.        ▓"
        elif new_cash == 200:
            host_line = "▓ Host: One hit! Not too ▓\n▓ shabby.                ▓"
        elif new_cash == 400:
            host_line = "▓ Host: Two hits! You're ▓\n▓ on a roll!             ▓"
        elif new_cash == 600:
            host_line = "▓ Host: Three hits!      ▓\n▓ That's 600 dollars.    ▓"
        else:
            host_line = "▓ Host: That's too many  ▓\n▓ hits to count!         ▓"
        print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓\n'''+
    string_line+'''
▓                        ▓''')
        if len(letter_guess) == 1:
            print('''▓ Your guess: '''+letter_guess+'''          ▓''')
        elif correct_guess == False:
            print('''▓ Your guess was wrong.  ▓''')
        elif correct_guess == True:
            print('''▓ You guessed it!        ▓''')
        print('''▓ Cash Won: $'''+cash_line+'''
▓                        ▓
'''+host_line+'''
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
        if new_cash >= 600 and letter_guess not in vowels:
            time.sleep(3)
            print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ Host: But that's not   ▓
▓ all, three hits or     ▓
▓ higher means a bonus   ▓
▓ round. Pick a door!    ▓
▓                        ▓
▓    ░░     ▒▒     ▓▓    ▓
▓  1 ░o   2 ▒o   3 ▓o    ▓
▓    ░░     ▒▒     ▓▓    ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
            prize_door = random.randint(1,3)
            door_choice = 0
            show_door = [1,2,3]
            print("Type door 1, 2, or 3:")
            while door_choice == 0:
                user_input = take_input()
                if user_input == "DOOR 1" or user_input == "1":
                    door_choice = 1
                    del show_door[0]
                elif user_input == "DOOR 2" or user_input == "2":
                    door_choice = 2
                    del show_door[1]
                elif user_input == "DOOR 3" or user_input == "3":
                    door_choice = 3
                    del show_door[2]
                else:
                    print("Invalid input.")
            if prize_door in show_door:
                index = show_door.index(prize_door)
                del show_door[index]
            show_door_2 = str(random.choice(show_door))
            print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ Host: Nice choice,     ▓
▓ door number '''+str(door_choice)+'''.         ▓
▓ Door '''+show_door_2+''' has no prize.   ▓
▓ Stay or switch?        ▓
▓                        ▓
▓    ░░     ▒▒     ▓▓    ▓''')
            if show_door_2 == "1":
                print("▓  X ░o   2 ▒o   3 ▓o    ▓")
            elif show_door_2 == "2":
                print("▓  1 ░o   X ▒o   3 ▓o    ▓")
            else:
                print("▓  1 ░o   2 ▒o   X ▓o    ▓")
            print('''▓    ░░     ▒▒     ▓▓    ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
            choice = ""
            print("Type stay or switch:")
            while choice == "":
                user_input = take_input()
                if user_input == "STAY":
                    choice = "▓ stay. The prize was    ▓"
                elif user_input == "SWITCH":
                    choice = "▓ switch. The prize was  ▓"
                else:
                    print("Invalid input.")
            if choice == "▓ stay. The prize was    ▓":
                final_door = door_choice
            elif door_choice == 1 and show_door_2 == '2':
                final_door = 3
            elif door_choice == 1 and show_door_2 == '3':
                final_door = 2
            elif door_choice == 2 and show_door_2 == '1':
                final_door = 3
            elif door_choice == 2 and show_door_2 == '3':
                final_door = 1
            elif door_choice == 3 and show_door_2 == '2':
                final_door = 1
            elif door_choice == 3 and show_door_2 == '1':
                final_door = 2
            print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ Host: You decided to   ▓
'''+choice+'''
▓ behind door number '''+str(prize_door)+'''.  ▓''')
            if final_door != prize_door:
                print('''▓ Better luck next time. ▓
▓                        ▓''')
            else:
                print('''▓ Congrats! You win      ▓
▓ $1000!                 ▓''')
                cash_won += 1000
            cash_line = (str(cash_won)+"                       ")[:12]+"▓"
            print('''▓                        ▓
▓ Cash Won: $'''+cash_line+'''
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')

    cash_line = (str(cash_won)+"                        ")[:19]+"▓"
    print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ Your winnings amount   ▓
▓ to $'''+cash_line+'''
▓                        ▓''')
    if cash_won < 0:
        print('''▓ Host: Yikes.           ▓
▓                        ▓''')
    elif cash_won == 0:
        print('''▓ Host: Dead even!       ▓
▓                        ▓''')
    else:
        print(random.choice(host_compliments)+'''
▓                        ▓''')
    print('''▓ Hosted by Señor Host   ▓
▓ PRESS ENTER TO GO HOME ▓
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')

#MAIN LOOP
print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓   ╔╗║ ║═╦═║ ║╔═╗╔╗ ║   ▓
▓   ╠╝╚═╣ ║ ╠═╣║ ║║╚╗║   ▓
▓   ║  ═╝ ║ ║ ║╚═╝║ ╚╝   ▓
▓         ╔═╗╔══         ▓
▓         ║ ║╚═╗         ▓
▓         ╚═╝══╝         ▓
▓  PRESS ENTER TO START  ▓
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
input()
while shut_down == False:
    print(app_select)
    app_select2 = False
    while app_select2 == False:
        app_select = True
        user_input = take_input()
        if user_input == 'WHEEL OF FORTUNE' or user_input == 'WHEEL' or user_input == 'FORTUNE':
            wheel_of_fortune()
        elif user_input == 'GALLERY':
            gallery()
        elif user_input == 'CALC' or 'CALCULATOR':
            calculator()
        elif user_input == 'EXIT' or user_input == 'SHUT DOWN' or user_input == 'SHUTDOWN':
            shut_down = True
            print('''▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                        ▓
▓ System shutdown...     ▓'''+(5*"\n▓                        ▓")+'''\n▓ Goodbye.               ▓
▓                        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓''')
        else:
            print("Invalid input.")
            app_select2 = False
