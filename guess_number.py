import random  # for making random choices of computer number
# window ui creation by following

target = random.randint(1,100)

import tkinter as tk
from tkinter import *

# initializing the window for game
game = tk.Tk()
game.title("Game : Guess The Number")
game.configure( bg = "#121212")
game.option_add("*Font",("Impact",20))

# Creating frame for the title 
title_frame = Frame(game)

# creating label for the label
title_label = tk.Label(title_frame, text="Guess The Number Game",font=("Impact", 28), bg = "#121212", fg="#E0E0E0")

# seting title frame and in that title will be inside that frame
title_frame.pack()
title_label.pack()

# craeting frame to ask user the number
User_frame = Frame(game)


# Asking the 
que_label = Label(User_frame, text="Enter the number : ",font=("Arial Narrow", 24), bg = "#121212", fg="#E0E0E0")


# Taking number from the user
ans_num = Entry(User_frame, width=2,font=("Arial Narrow", 24), bg = "#121212", fg="#E0E0E0")

# creating a function to check the number is same or not??
def check():
    guess = ans_num.get()
    answer = int(guess)
    if (target == answer):
        right()
        ans_num.insert()
    else:
        if(target < answer):
            hint = "\nHint : Your Number was too Small.Take a Bigger guess."
            wrong(hint)
        else:
            hint = "\nHint : Your Number was too big.Take a Smaller guess."
            wrong(hint)


# creating some function according to choise
def right():
    msg = "✅ Congratulations! 🎉 You guessed the number correctly!"
    msg_label.configure(text = msg,bg = "#121212", fg = "#00FF00")
    done_btn.destroy()
    msg_label.pack()
    replay_btn.pack()

def wrong(hint):
    msg = "❌ Oops! Wrong guess. Try again!" + hint
    msg_label.configure(text = msg,bg = "#121212", fg = "#FF4500")
    done_btn.destroy()
    msg_label.pack()
    replay_btn.pack()

# Creating an msg for user according to the input
msg_label = Label(game, text = "uierhhiuheui",bg = "#121212", fg="#E0E0E0")


# setting frame elements
User_frame.pack()
que_label.grid(column = 1, row = 1)
ans_num.grid(column = 2, row = 1, padx=2)

# Creating A submit Button
done_btn = Button(game, text=" Submit ", bg = "#00BFFF", fg="#E0E0E0",command=check)
done_btn.configure(font = ("Imapct", 24))
done_btn.pack()

# Replay button
replay_btn = Button(game, text=" Replay ", bg = "#00BFFF", fg="#E0E0E0")
replay_btn.configure(font = ("Imapct", 24))

game.mainloop()