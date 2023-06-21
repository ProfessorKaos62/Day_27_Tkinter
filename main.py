from tkinter import *

window = Tk()
window.title('Miles to Km')
window.minsize(width=100, height=100)

kilos = 0


def button_clicked():
  kilos = round(float(input.get()) * 1.609, 2)
  kilometers.config(text=f"{kilos}")


my_label = Label(text='is equal to', font=('Ariel', 16))
my_label.grid(column=0, row=1)

input = Entry(width=15)
input.grid(column=1, row=0)

miles = Label(text='Miles', font=('Ariel', 16))
miles.grid(column=2, row=0)

kilometers = Label(text=f'{kilos}', font=('Ariel', 16))
kilometers.grid(column=1, row=1)

km = Label(text='Km', font=('Ariel', 16))
km.grid(column=2, row=1)

my_button = Button(text='Calculate', command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()