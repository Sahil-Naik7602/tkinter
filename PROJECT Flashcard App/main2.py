import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card,flipper
    window.after_cancel(flipper)
    current_card = random.choice(to_learn)
    canvas_flashcard.create_image(500, 300, image=card_front_img)
    canvas_flashcard.create_text(500,150,text="French", font=("Calibiri",30,"italic"))
    canvas_flashcard.create_text(500,275,text=current_card["French"], font=("Calibiri",50,"normal"))
    flipper = window.after(3000,flip_card)

def flip_card():
    canvas_flashcard.create_image(500, 300, image = card_back_img)
    canvas_flashcard.create_text(500,150,text="English", font=("Calibiri",30,"italic"),fill="white")
    canvas_flashcard.create_text(500,275,text=current_card["English"], font=("Calibiri",50,"normal"),fill="white")

def known_word():
    to_learn.remove(current_card)
    next_card()
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv")
    
window=Tk()
window.title("Flashcard App Capstone Project")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
flipper = window.after(3000,flip_card)

canvas_flashcard = Canvas(width=1000,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_flashcard.grid(row=0,column=0,columnspan=2)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR,command=known_word)
right_button.grid(row=1,column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img ,bg=BACKGROUND_COLOR, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
next_card()

window.mainloop()
