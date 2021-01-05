from tkinter import *

import requests

def aftetap():
     response = requests.get(url="https://api.kanye.rest/")
     data=response.json()
     canvas.itemconfig(text, text= data['quote'])

FONT_NAME = "Courier"

window= Tk()
window.title("Kanye Says....")
window.config(padx=50, pady=50)

canvas = Canvas(width=350, height=450)
logo = PhotoImage(file="background.png")
canvas.create_image(150, 200, image=logo)
text = canvas.create_text(150, 120, text="Kanye Text", width=250,font=(FONT_NAME, 15, "bold") )
canvas.grid(column=0, row=0)


head = PhotoImage(file="kanye.png")
headbutton = Button(image=head, highlightthickness=0, command= aftetap)
headbutton.grid(column=0, row=1)



window.mainloop()