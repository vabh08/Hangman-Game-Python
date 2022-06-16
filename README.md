# Hangman-Game-Python

The objective of this project is to create a GUI based Hangman game. To build this, you will need intermediate understanding of Tkinter library and PIL’s GUI elements, and basic understanding of the random and screeninfo libraries.

Project Prerequisites:

To build this project, we will need the following libraries:

1. Tkinter – To create the GUI.
2. PIL (Pillow) – This is Python’s Image Library used for image manipulation. Here, we will use it to convert the Hangman progress images to PhotoImage format, which allows them to be displayed on Tkinter.
3. screeninfo.get_monitors() – To get the info of the screen’s dimension to set the height and width of the GUI window and its elements.
4. random.choice() – To get a random word from our list that the user of the game will guess.
5. os – To exit the script.

Tkinter Elements used:

1. The Tk() class is used to initialize a GUI window. The attributes and methods that need to be set during initialization are:

a. .title() method is used to set a title to the window.

b. .geometry() method is used to set the geometry of the window.

c. .resizable() method is used to allow/forbid the user to resize the window.

d. .update() and .mainloop() methods are used to prevent the window from closing milliseconds after it opens.

Note: These are the last lines that will be executed that edit the window in any way.

2. The Label widget is used to display static text to the window.

a. The image parameter is used to specify the PhotoImage object that will be used in place of/along with text in the Label.

3. The Button class is used to add a button to the window that executes a function as a command when pressed.

a. The command parameter is the function to be executed when the button is pressed.

4. The .place() method is used to place the widget it is associated with as though it is on a Cartesian plane.

a. The anchor parameter specifies the origin of the Cartesian for that widget. It can be a corner or a side of the root window.

b. The relx, rely parameters are used to set the horizontal and vertical offsets of the widget as a float number between 0.0 and 1.0

c. The x, y parameters are used to set the horizontal and vertical offsets of the widget

    The master parameter is the parent widget of the class it is associated with.
    The text parameter is the text to be displayed.
    The font parameter is used to specify the font family and effects to the text.
    The bg parameter is used to give a background color.

Project File Structure:

These are the files used in this project:

1. main.py – This will be our main python file.

2. words.txt – This is the word file where all the words to guess will be there.

3. Steps Images (folder): In this folder, we have kept all the progress images that will be displayed as the user guesses an incorrect letter

a. Step 0.png – Image to be displayed in the beginning where only the basic setup is visible.

b. Step 1.png – Image to be displayed after 1 incorrect guess. No body part is visible.

c. Step 2.png – Image to be displayed after 2 incorrect guesses. Only the head is visible.

d. Step 3.png – Image to be displayed after 3 incorrect guesses. The torso appears.

e. Step 4.png – Image to be displayed after 4 incorrect guesses. The arms appear.

f. Step 5.png – Image to be displayed after 5 incorrect guesses. The legs appear and Man gets scared!

g. Step 6.png – Image to be displayed after the sixth incorrect guess. Man is hung in this step and the user loses!

h. Winner.png – Image to be displayed after the user has successfully guessed the word with 1 or more incorrect guesses remaining. A banner with Congratulations appears, and man thanks you for saving his life.

Here are the steps you will need to execute to build this project:

1. Importing all the necessary modules

2. Setting the variables and getting the monitor’s height and width

3. Creating all the functions

4. Initializing the GUI window, placing components in it and asking if the user wants to play or not

Importing all the necessary modules:

    The get_monitors() function will be used to get the information of the local machine’s monitors.
    The system() function will be used (here) only to rerun our Python file if the user decides to reset the game.

Setting the variables and getting the monitor’s height and width:

    We will define the get_word function later.
    Slice the get_monitors() so that we can get the dimensions of the monitor that we are using.
    We decreased the width and height so the game doesn’t go into full screen mode and hides the taskbar.
    The incorrect_guesses and correct_guesses are used to keep a counter as to how many correct and incorrect guesses have been made by the user.
    We have decremented the value of word_length by 1 because in our words.txt file, the last character of all the words is a blank space by default.

Creating all the functions:

    In this step, we will create all the functions used in our game.
    The instructions() function simply displays a mb.showinfo() box detailing some of the rules and instructions of the game.
    The reset() function asks the user if they really want to reset the game using a mb.askyesno() box. If they want to, we will destroy our root window, and use the system() function of the OS library to rerun our main.py python file.
        How mb.askyesno() works is that if the user presses the “Yes” button, it returns True and returns False if the “No” button is pressed.
    The end_game() function does the same thing as the reset() function, but if the user wants to end the game, we will use the built-in exit() function to end our Python then-and-there.
    In the get_word() function, we will parse through our word.txt file by opening it in the read mode and store all the words in the file (lines) in a list.
    The word for our game will be a word that will be chosen at random by the choice() function of the random library, which the user will need to guess.
    Our main() function, which will essentially do everything to be done when a user presses any letter button, might seem complex, but is very easy once comprehended.
        Whenever the user presses any button, the button will record itself as the argument to its command parameter’s argument (any function) [We’ll get into it later when we talk about the GUI window].
        In this function, we will firstly get all the PhotoImage objects and variables to be usable in the function using the global keyword.
        Then, we will check if btn[“text”] (text inside the button) is an element in li_word (the list form of our word), and if it is, we will make that button’s bg color as Spring Green and get all the indices where that letter is present in the word.
        Then we will parse through that list of indices we made earlier, and change the text of the corresponding letter Label to the character of the word, thus revealing it and we will increment the value of correct_guesses by one.
        If the button pressed isn’t in the word, then it will turn red and we will increment the value of incorrect_guesses by one, and change the PhotoImage object visible to one that shows the next step.
        After this conditional pair, we will configure the button to disable, meaning that it can no longer be pressed.
        Eventually, if the value of correct_guesses is equal to the length of our word, the user will win and the image will change accordingly. And if the value of incorrect_guesses maximises, the user will lose and Man will die.

Initializing the GUI window, placing components in it and asking if the user wants to play or not:

    In this step, we will create our GUI window of the game.
    After we define the heading label, we will provide the user with a storyline and ask if they want to play. If they do, we will continue but if they don’t, we’ll use exit() function to end our script.
    Then we will open our images in the “Steps Images” folder and convert them to PhotoImage objects which will be displayed by the image_lbl, which is a Label widget.
    We will then place the word on the window, towards the right of the image in the form of underscores to denote the number of characters it is.
    At the bottom side, we will have all the buttons that the user needs to press in order for the game to progress.
        The built-in exec() is used to execute what is provided to it as an argument as a python script.
        The button_details variable that we defined earlier contains the latter part of the variable name, text to be displayed,
        x-offset and y-offset of the button respectively in each nested list.
        Using the exec() function, we will successfully create all the buttons and provide those buttons as arguments to the function we put in in the command parameter while defining the button.
    On the top right side of the window, we have 3 buttons that will execute the instructions(), reset(), and end_game() functions when pressed.

