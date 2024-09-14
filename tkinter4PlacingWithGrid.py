from tkinter import *

#setup of screen
my_window = Tk()
my_window.minsize(width=600, height=500)
my_window.title("Items are placed around by place")
my_window.config(padx=20, pady=20)
#creating a label
my_label = Label(text="I am a label, i represent text.")
my_label.config(font=("Times New Roman", 20, "italic"))
my_label.grid(row=0,column=0)
my_label.config(padx=20, pady=20)
#in the place method the scale is kind of weired, it does not work like your tradition x, y graph, but x and y still control the value of horizontail and vertical axis

#creating a button and position it somewhere middle of the screen
button = Button(text="Do Not Click Me, Please No!!")
button.grid(row=1,column=1)
button.config(padx=20, pady=20)
#creating the input method lastly a nd placing it in middle of screen
input = Entry()
# input.config(width=15)
input.grid(row=0,column=2)
input.insert(END,string="Some text to begin with.")


#not that the grid and pack can not be used with one another as they are in compatible

#creating a spinbox to complete the challenge
spinbox = Spinbox(from_=0, to=10, width=5)
# spinbox.pack()
# using the code above would give an error as pack and grid does not work together at all
spinbox.grid(row=2, column=3)










#always must be placed towards the end,keeps the program running, other wse the screen would terminate right away
my_window.mainloop()