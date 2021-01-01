from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
raps = 0
i=0


# ---------------------------- TIMER ------------------------------- #
def starttime():
    global raps
    raps += 1
    if raps % 8 == 0:
        count_down(20 * 60)
    elif raps % 2 == 0:
        count_down(5 * 60)
    else:
        count_down(25 * 60)


# ---------------------------- COUNTDOWN ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(texttime, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        starttime()
        if raps %2==0:
            global i
            i += 1
            checkmark = Label(text="✔️", fg="GREEN", bg="YELLOW")
            checkmark.grid(column=1, row=4+i)

# ---------------------------- UI ------------------------------- #


window = Tk()
window.title("Pomorodo")
window.config(padx=150, pady=100, bg="YELLOW")

label = Label(text="Pomorodo", fg=GREEN, bg="YELLOW", font=(FONT_NAME, 50, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=210, height=240, bg="YELLOW", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(107, 120, image=tomato_img)
texttime = canvas.create_text(107, 130, text="00:00", fill="YELLOW", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

startButton = Button(text="Start", fg=GREEN, bg="RED", font=(FONT_NAME), command=starttime)
startButton.grid(column=1, row=3)

window.mainloop()
