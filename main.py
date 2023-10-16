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
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    sort_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        timer_label["text"] = "Work"
        count_down(work_sec)

    elif REPS % 2 == 0:
        timer_label["text"] = "Short Break"
        timer_label["fg"] = PINK
        count_down(sort_break_sec)

    elif REPS % 8 == 0:
        timer_label["text"] = "Long Break"
        timer_label["fg"] = RED
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS
    minute_count = math.floor(count / 60)
    second_count = count % 60

    if second_count < 10:
        second_count = f'0{second_count}'

    if minute_count < 10:
        minute_count = f'0{minute_count}'

    canvas.itemconfig(timer_text, text=f"{minute_count}:{second_count}")

    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        start_timer()
        if REPS % 2 == 0:
            ticks = "✔ " * (REPS - 1)
            tick_label.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=220, height=223, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 50))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

tick_label = Label(fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW)
tick_label.grid(column=2, row=4)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
