from tkinter import *
import random

display = Tk()

display.geometry("800x400")

# main function that will generate the password
pass_str = StringVar()
pass_length = IntVar()
pass_length.set(0)

def pass_generator():
    pass_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
                '9', '0', ' ', '!', '@', '#', '&']

    password = ""

    for x in range(pass_length.get()):
        password += random.choice(pass_list)
    
    pass_str.set(password)

# functions that will open a text file to write on it and save text function
file_state = False
def open_text():
    global file_state
    file_state = True
    text_file = open("saved_password.txt", "r")
    passwords = text_file.read()
    saved_password.insert(END, passwords)
    text_file.close


def save_text():
    if file_state:
        text_file = open("saved_password.txt", "w")
        text_file.write(saved_password.get(1.0, END))
        text_file.close()

saved_password = Text(display, height=10,width=40)
saved_password.pack()
# draw some button and labels for user inputs
Label(display, text="Password Generator", font="Times 28 bold").pack()

Label(display, text="Enter Length for the password").pack()

Entry(display, textvariable=pass_length).pack() 

Button(display, text="Generate Password", command=pass_generator).pack()

Entry(display, textvariable=pass_str).pack()

Button(display, text="Open password file", command=open_text).pack()

Button(display, text="Save File", command=save_text).pack()

display.mainloop()