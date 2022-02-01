import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"

#-------------------ITTERING THROUGH INPUTS-----------------#
data = pd.read_csv("data/french_words.csv")
French_words = data.French
displayed_french_word = random.choice(French_words.tolist())

#-------------------RIGHT AND WRONG FUNCTIONS-----------------#
seen_once=[]

def right():
    new_french_word = random.choice(French_words.tolist())
    if new_french_word not in seen_once:
        canvas_flashcard.create_image(500, 300, image=card_front_img)
        canvas_flashcard.create_text(500,150,text="French", font=("Calibiri",30,"italic"))
        canvas_flashcard.create_text(500,275,text=f"{new_french_word}", font=("Calibiri",50,"normal"))
        seen_once.append(new_french_word)
    else :
        new_french_word = random.choice(French_words.tolist())
        right()
    print(seen_once)
    
def wrong():
    displayed_english_meaning = data.English[data.French == seen_once[-1]].tolist()
    canvas_flashcard.create_image(500, 300, image = card_back_img)
    canvas_flashcard.create_text(500,150,text="English", font=("Calibiri",30,"italic"))
    canvas_flashcard.create_text(500,275,text=f"{displayed_english_meaning[0]}", font=("Calibiri",50,"normal"))
    print(seen_once)
    

#-------------------CREATING UI-----------------#
window=Tk()
window.title("Flashcard App Capstone Project")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

canvas_flashcard = Canvas(width=1000,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_flashcard.create_image(500, 300, image=card_front_img)
canvas_flashcard.create_text(500,150,text="French", font=("Calibiri",30,"italic"))
canvas_flashcard.create_text(500,275,text=f"{displayed_french_word}", font=("Calibiri",50,"normal"))
seen_once.append(displayed_french_word)
canvas_flashcard.grid(row=0,column=0,columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
right_button.grid(row=1,column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img ,bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong)
wrong_button.grid(row=1,column=0)

window.mainloop()

