from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

words = pd.read_csv("data/french_words.csv")
words_dict = words.to_dict(orient = "records")

def change_cards():
    canvas.itemconfig(image_id, image = card_back)
    canvas.itemconfig(title_id, fill = "white", text = "English")
    canvas.itemconfig(fr_word_id, fill = "white")

def random_word_selector():
    random_fr_word = random.choice(words_dict)
    print(random_fr_word)
    canvas.itemconfig(fr_word_id, text = random_fr_word['French'])
    canvas.itemconfig(title_id, text = "French")
    delay_id = window.after(3000, change_cards)

# --------------------------------- UI ----------------------------------------

window = Tk()
window.title("Flash Card Project")
window.configure(background=BACKGROUND_COLOR, padx = 50, pady = 50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file = "images/card_back.png")
card_front = PhotoImage(file = "images/card_front.png")
image_id = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title_id = canvas.create_text(400, 150, text = "", font = ("Arial", 40, "italic"))
fr_word_id = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"))


no_button_image = PhotoImage(file = "images/wrong.png")
yes_button_image = PhotoImage(file = "images/right.png")

no_button = Button(window, image = no_button_image, command = random_word_selector, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
no_button.grid(row = 1, column = 0)

yes_button = Button(image = yes_button_image, command = random_word_selector, highlightthickness = 0, highlightbackground = BACKGROUND_COLOR)
yes_button.grid(row = 1, column = 1)

random_word_selector()

window.after(3000, change_cards)
window.mainloop()
