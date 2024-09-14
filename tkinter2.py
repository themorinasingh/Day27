from tkinter import *

#first and foremost i need a screen, in this case a window

my_window = Tk()
my_window.minsize(width=720, height=480)
my_window.title("My_window = Tk()")

my_label = Label(text="my_label = Label(font=('Times New Roman', 30, 'bold'))", font=("Ariel", 25, "normal"))
# my_label.config(text="Test Font")
# my_label["text"] = "Test Font"
my_label.config(font=("Times New Roman", 30, "bold"))
my_label.pack()

def button_clicked():
    my_label["text"] = "Button Got Clicked"

my_button = Button()
my_button.config(text="Click Me")
my_button.pack()

input = Entry(width=20)
input.pack()

def button_clicked_2():
    # print(type(input.get()))
    my_label.config(text=input.get())

my_button["command"] = button_clicked_2




my_window.mainloop()