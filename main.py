from tkinter import *
import pandas 
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/italian_freq.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


def new_card():
    global current_card, flip_timer
    canvas.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_language, text=["Italian"], fill="black")
    canvas.itemconfig(card_word, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_backround, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_backround, image=card_back_image)


def known_card():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# tkinter Window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

# Flash card 
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_backround = canvas.create_image(400, 260, image=card_front_image)


# Flash card text
card_language = canvas.create_text(400, 190, text="Italian", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=("Ariel", 80, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Wrong Button
x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, border=0, command=new_card)
unknown_button.grid(column=0, row=1)

# Right Button
check_mark_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_mark_image, borderwidth=0, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

new_card()

window.mainloop()


