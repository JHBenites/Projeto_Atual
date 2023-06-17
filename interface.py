import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Aceitas?')
root.geometry('600x600')
root.configure(background='#ffc8dd')

global teste1
teste = 1

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('', 'tente o outro botão')

def denied():
    button_1.pack_forget()
    button_1.config(text='FOI')
    teste1 = False

margin = Canvas(root, width=500, bg='#ffc8dd', height=100,
               bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text='Você é noob?',
                fg='#590d22', font=('Montserrat', 14, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied,
                     relief=RIDGE, bd=3, font=('Montserrat', 12, 'bold'))

button_1.pack()
if teste1 == True:
    root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE,
                     bd=12, command=accepted, font=('Montserrat', 16, 'bold'))
button_2.pack()

root.mainloop()