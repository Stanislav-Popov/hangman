from start_game import start
from tkinter import *


window = Tk()
window['bg'] = "#fafafa"
window.wm_attributes('-alpha', 0.95)
window.title('Игра "Виселица"')
window.geometry('700x500')
# window.resizable(width=False, height=False)

canvas = Canvas(window, height=450, width=500)
canvas.pack()

frame = Frame(window)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheigh=0.7)

title = Label(frame, text='Давай сыграем?', font=40)
title.pack()

bstart = Button(window, text="Начать игру", padx='15', pady='6', font='15', command=start)
bstart.pack(expand=True, fill=BOTH)


window.mainloop()
