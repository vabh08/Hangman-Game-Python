from tkinter import *
import tkinter.messagebox as mb

from PIL import ImageTk, Image
from screeninfo import get_monitors
from random import choice
from os import system

# Basic Hangman function
def get_word():
    words = []

    with open('words.txt', 'r') as wordlist:
        for line in wordlist:
            words.append(line)

    chosen_word = choice(words)

    return chosen_word


def main_function(btn: Button):
    global image_lbl, li_word, correct_guesses, incorrect_guesses
    global step_1, step_2, step_3, step_4, step_5, step_6

    if btn['text'] in li_word:
        btn.config(bg='SpringGreen', fg='Black')
        indices = [indx for indx, val in enumerate(li_word) if val == btn['text']]
        for index in indices:
            exec(f'ltr_{index}["text"] = btn["text"]')
            correct_guesses += 1

    else:
        btn.config(bg='Red', fg='White')
        incorrect_guesses += 1
        exec(f'image_lbl.config(image=step_{incorrect_guesses})')

    btn.config(state='disabled')

    if correct_guesses == word_length:
        image_lbl.config(image=won_image)
        mb.showinfo('Congratulations!', 'You have won!\nMan was right to believe you and you have proved it!\nCongratulations!')
        root.destroy()

    if incorrect_guesses == 6:
        mb.showerror('Man\'s dead!', 'Man counted on you to save him, and you have let him down!')
        root.destroy()


# Command functions for the buttons at the top-right of the screen
def instructions():
    mb.showinfo('',
"""The instructions are simple:
You have 6 chances of saving Man, if you get 6 incorrect guesses while trying to guess the detective's word, Man's going to be hung. 
If you make less than 6 incorrect guesses while guessing the word, you will be successful in saving Man's life and he will be eternally grateful to you.""")


def end_game():
    surety = mb.askyesno('', 'Are you sure you want to exit the game? \nYour progress will not be saved')

    if surety:
        root.destroy()


def reset():
    surety = mb.askyesno('', "Are you sure you want to reset your game?")

    if surety:
        root.destroy()
        system('python main.py')


# Variables
buttons_details = [["a", "A", 25, 800], ["b", "B", 125, 800], ["c", "C", 225, 800], ["d", "D", 325, 800],
                   ["e", "E", 425, 800], ["f", "F", 525, 800], ["g", "G", 625, 800], ['h', "H", 725, 800],
                   ['i', "I", 825, 800], ['j', "J", 925, 800], ['k', "K", 1025, 800], ['l', "L", 1125, 800],
                   ['m', "M", 1225, 800], ['n', "N", 25, 900], ['o', "O", 125, 900], ['p', "P", 225, 900],
                   ['q', "Q", 325, 900], ['r', "R", 425, 900], ['s', "S", 525, 900], ['t', "T", 625, 900],
                   ['u', "U", 725, 900], ['v', "V", 825, 900], ['w', "W", 925, 900], ['x', "X", 1025, 900],
                   ['y', "Y", 1125, 900], ['z', "Z", 1225, 900]]

word = get_word()
word_length = len(word)-1

correct_guesses = 0
incorrect_guesses = 0

li_word = [char.upper() for char in word]
# Getting the computer screen's dimensions
monitor = get_monitors()[0]

width = monitor.width - 600
height = monitor.height - 100

# Initializing the window
root = Tk()
root.title('Python Hangman creator-Vaibhav')
root.geometry(f'{width}x{height}')
root.resizable(0, 0)
root.config(bg='White')
root.positionfrom('user')

# Title Label
Label(text='Python Hangman Game\ncreator-\nVaibhav', font=("Comic Sans MS", 22), bg='White').place(relx=0.25, y=0)

# Asking if the user wants to play
start_ques = mb.askyesno('Storyline',
'''Man — yes, that's his name — has been wrongfully imprisoned and is about to be given the capital punishment.
However, the old detective came across some proof that proves Man is innocent. So, the detective wants Man to decide 
his fate and has asked Man to guess a random word he has chosen fully aware that Man himself cannot guess this word 
because it is too tough for him. And Man has asked you to guess this word for him, and has literally given his life to you.
You will have 6 lifelines to save Man. If you get 6 incorrect guesses, Man's dead but if you get the word before 
these lifelines end, Man will live and be eternally grateful to you.
\nWhat do you say, feeling like saving an innocent's life today?''')

if not start_ques:
    root.destroy()
    exit()

# Creating all the steps images in PhotoImage format
step_0 = ImageTk.PhotoImage(Image.open('Steps Images/Step 0.png'))
step_1 = ImageTk.PhotoImage(Image.open('Steps Images/Step 1.png'))
step_2 = ImageTk.PhotoImage(Image.open('Steps Images/Step 2.png'))
step_3 = ImageTk.PhotoImage(Image.open('Steps Images/Step 3.png'))
step_4 = ImageTk.PhotoImage(Image.open('Steps Images/Step 4.png'))
step_5 = ImageTk.PhotoImage(Image.open('Steps Images/Step 5.png'))
step_6 = ImageTk.PhotoImage(Image.open('Steps Images/Step 6.png'))
won_image = ImageTk.PhotoImage(Image.open('Steps Images/Winner.png'))

image_lbl = Label(root, image=step_0, bg='White')
image_lbl.place(relx=0.15, rely=0.1)

# Placing the word on the window
Label(root, text='Word to guess:', font=("Georgia", 20, 'bold'), bg='White').place(relx=0.635, rely=0.4)

x = 0.6
i = 0
while i < word_length:
    exec(f'''ltr_{i} = Label(root, text="_", bg="White", font=("Georgia", 30)); ltr_{i}.place(relx={x}, rely=0.45)''')
    x += 0.03
    i += 1

# Creating all the letter buttons
for button in buttons_details:
    exec(f'''{button[0]}_btn = Button(root, text=button[1], width=8, height=2, bg="DeepSkyBlue", 
         command=lambda: main_function({button[0]}_btn))''')
    exec(f'{button[0]}_btn.place(x=button[2], y=button[3])')

Button(root, text='INSTRUCTIONS', font=("PlayfairDisplay", 12, 'bold'), bg='DeepSkyBlue',
       command=instructions).place(x=1125, y=100)

Button(root, text='EXIT', font=("PlayfairDisplay", 12, 'bold'), width=13, bg='DeepSkyBlue',
       command=end_game).place(x=1125, y=175)

Button(root, text='RESET', font=("PlayfairDisplay", 12, 'bold'), width=13, bg='DeepSkyBlue',
       command=reset).place(x=1125, y=250)

# Finalizing the window
root.mainloop()