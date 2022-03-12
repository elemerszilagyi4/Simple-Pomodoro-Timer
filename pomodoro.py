from tkinter import *

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
check_marks = ""
running = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    reseting()


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_time = 1500
    small_break = 300
    big_break = 1200
    global reps
    reps += 1
    if reps % 2 == 1:
        label.config(text="Work!", font=(FONT_NAME, 35, "bold"))
        count_down(work_time)
    elif reps % 2 == 0 and reps != 8:
        label.config(text="Take a break!", font=(FONT_NAME, 35, "bold"))
        count_down(small_break)
    else:
        label.config(text="Take a break!", font=(FONT_NAME, 35, "bold"))
        count_down(big_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def reseting():
    global running
    global check_marks
    global reps
    reps = 0
    check_marks = ""
    window.after_cancel(running)
    canvas.itemconfig(timer, text="")
    label.config(text="Timer")
    check_mark.config(text="")


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    elif seconds == 0:
        seconds = "00"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global running
        running = window.after(1000, count_down, count - 1)
    else:
        global check_marks
        print(label["text"])
        if label["text"] == "Work!":
            check_marks = check_marks + "✔"
            check_mark.config(text=check_marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=50, pady=50, bg=YELLOW)

window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer = canvas.create_text(103, 132, text="", fill="#9bdeac", font=(FONT_NAME, 35, "bold"))

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)


check_mark = Label(text="", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN, pady=40)

reset = Button(text="Reset", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"), highlightthickness=0,
               command=reset_timer)
start = Button(text="Start", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"), highlightthickness=0,
               command=start_timer)

label.grid(row=0, column=0, columnspan=3)

start.grid(row=2, column=0)
reset.grid(row=2, column=2)
canvas.grid(row=1, column=1)
check_mark.grid(row=2, column=1)

window.mainloop()
