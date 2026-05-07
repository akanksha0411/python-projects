from tkinter import *
from tkinter import simpledialog

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
timer_g = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_g
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_g = window.after(1000, count_down, count - 1)
    else:
        mark = "✓"
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        checkmark_icon.configure(text = mark)
        start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps%2 !=0:
        count_down(work_min * 60)
        timer.configure(text = "Work Mode", fg=GREEN)
        print(reps)
    if reps%8 == 0:
        count_down(1 * 60)
        timer.configure(text="Long Break", fg=RED)
        print(reps)
    if reps%2 == 0:
        count_down(1 * 60)
        timer.configure(text="Short Break", fg=PINK)
        print(reps)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer_g
    window.after_cancel(timer_g)
    timer.configure(text = "Timer", font = (FONT_NAME, 50, "bold"), fg = GREEN, bg = YELLOW)
    checkmark_icon.configure(text = "")
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=0, bg = YELLOW)

canvas = Canvas(window, width=250, height=250, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file = "tomato.png")
canvas.create_image(125, 125, image=image)
timer_text = canvas.create_text(125, 140, text ="00:00", fill = "white", font = (FONT_NAME, 40, "bold"))
canvas.grid(column = 1, row = 1)

timer = Label(window, text = "Timer", font = (FONT_NAME, 50, "bold"), fg = GREEN, bg = YELLOW)
timer.grid(column = 1, row = 0)

work_min = simpledialog.askinteger("Input", "Enter Minutes")

start_button = Button(window, text = "Start", command = start_timer, bg=YELLOW, font = (FONT_NAME, 10, "bold"), highlightbackground=YELLOW)
start_button.grid(column = 0, row = 2)

reset_button = Button(window, text = "Reset", command = reset_timer, bg=YELLOW, font=(FONT_NAME, 10, "bold"), highlightbackground=YELLOW)
reset_button.grid(column = 2, row = 2)

checkmark_icon = Label(window, font= (FONT_NAME,50, "bold"), fg = GREEN, bg = YELLOW)
checkmark_icon.grid(column = 1, row =3)


window.mainloop()
