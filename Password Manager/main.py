from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #r

def generating():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    symc = random.randint(2, 5)
    numc = random.randint(2, 5)
    letc = random.randint(2, 5)
    l = []
    for i in range(0, symc):
        r = random.choice(symbols)
        l.append(r)
    for i in range(0, numc):
        r = random.choice(numbers)
        l.append(r)
    for i in range(0, letc):
        r = random.choice(letters)
        l.append(r)
    m = len(l)
    v = []
    for j in range(0, m):
        v.append(l[j])
    str1 = ""
    for ele in v:
        str1 += ele
    final = str(str1)

    entrypass.insert(0, final)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = entryweb.get()
    email = entrymail.get()
    pword = entrypass.get()

    try:
        if len(entryweb) == 0 or len(entrymail) == 0:
            messagebox.showinfo(title="OOPS", message="Few Fields are empty")
        else:
            messagebox.showinfo(title="Message", message="Successfull")
    except:
        messagebox.showinfo(title="Message", message="Successfull")

    with open("data.txt", "a") as data_file:
        data_file.write(f"{web}  |  {email}  |  {pword}\n")
        entryweb.delete(0, END)
        entrypass.delete(0, END)
        entrymail.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=2)

email = Label(text="Email")
email.grid(column=0, row=3)

password = Label(text="Password")
password.grid(column=0, row=4)

blank = Label(text=" ")
blank.grid(column=1, row=4)

entryweb = Entry(width=52)
entryweb.insert(END, string="")
entryweb.grid(column=1, row=2, columnspan=2)

entrymail = Entry(width=52)
entrymail.insert(END, string="")
entrymail.grid(column=1, row=3, columnspan=2)

entrypass = Entry(width=32)
entrypass.insert(END, string="")
entrypass.grid(column=1, row=4)

generate = Button(text="Generate Password", command=generating)
generate.grid(column=2, row=4, )

add = Button(text="ADD", width=36, command=save)
add.grid(column=1, row=5, columnspan=2)

window.mainloop()
