from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkbox=""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN, bg=YELLOW)
    tick_label.config(text="")
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps %8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break",font=(FONT_NAME,30,"bold"),fg=GREEN, bg=YELLOW)
    elif reps%2!=0:
        count_down(work_sec)
        timer_label.config(text="WORK TIME",font=(FONT_NAME,30,"bold"),fg=RED, bg=YELLOW)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break",font=(FONT_NAME,30,"bold"),fg=PINK, bg=YELLOW)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checkbox
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        if reps % 2 !=0:
            checkbox += "✔"
            tick_label.config(text=checkbox)
        start_time()
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

canvas = Canvas(height=224, width=200, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=2,row=2)

timer_label = Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN, bg=YELLOW)
timer_label.grid(column=2,row=1)
timer_label.config(pady=20,highlightthickness=0)

tick_label = Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
tick_label.grid(column=2,row=3)
tick_label.config(pady=10,highlightthickness=0)

start_button = Button(text="START",command=start_time)
start_button.grid(column=1,row=3)

reset_button = Button(text="RESET",command= reset)
reset_button.grid(column=3,row=3)

window.mainloop()


