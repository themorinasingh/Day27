import tkinter

#creating a window in tkinter
window = tkinter.Tk()
#this code will gove our window a title
window.title("My name is window")
#customizing the size of the window
window.minsize(width=500, height=500)

#creating a label, it is comparable to turtle
my_label = tkinter.Label(text="My First Label", font=("Ariel", 25, "bold"))
#packer will pack the label on screen and you could use a few keywords like side, expand
my_label.pack(side="right")











#this will allow my screen to stay on and listen for activity from user on the window
window.mainloop()