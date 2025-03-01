import random  # for making random choices of computer number
# window ui creation by following
import tkinter as tk
from tkinter import *

# initializing the window for game
game = tk.Tk()
game.title("Game : Guess The Number")
game.configure(bg="black")
game.option_add("*Font",("Arial Narrow",20))


# Creating frame for the title 
title_frame = Frame(game)

# creating label for the label
title_label = tk.Label(title_frame, text="Guess The Number Game",font=("Impact", 28), fg="white", bg = "black")

# seting title frame and in that title will be inside that frame
title_frame.pack()
title_label.pack()

# craeting frame to ask user the number
User_frame = Frame(game)
que_label = Label(User_frame, text="Enter the number : ",font=("Arial Narrow", 24), fg="", bg = "black")
ans_num = Entry(User_frame)

# setting frame elements
User_frame.pack()
que_label.grid(column = 1, row = 1)
ans_num.grid(column = 2, row = 1)

done_btn = Button(game, text=" Submit ",font=("Imapct", 24), fg="white", bg = "green", padx=5, pady=1)
done_btn.pack()

game.mainloop()