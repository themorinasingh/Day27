from tkinter import *

#setup of screen
my_window = Tk()
my_window.minsize(width=600, height=500)
my_window.title("Items are placed around by place")

#creating a label
my_label = Label(text="I am a label, i represent text.")
my_label.config(font=("Times New Roman", 20, "italic"))
my_label.place(x=180,y=90)
#in the place method the scale is kind of weired, it does not work like your tradition x, y graph, but x and y still control the value of horizontail and vertical axis

#creating a button and position it somewhere middle of the screen
button = Button(text="Do Not Click Me, Please No!!")
button.place(x=190, y= 120)

#creating the input method lastly a nd placing it in middle of screen
input = Entry()
input.place(x=200, y=150)














#always must be placed towards the end,keeps the program running, other wse the screen would terminate right away
my_window.mainloop()