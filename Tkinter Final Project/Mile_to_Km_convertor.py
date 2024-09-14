from tkinter import *

#setup our window
window = Tk()
window.title("Miles TO Km Converter")
window.minsize(width=300, height= 150)
window.config(padx=20,pady=20)

#creating out input
num_miles = Entry()
num_miles.config(width=15)
num_miles.focus()
num_miles.grid(row=0,column=1)

#creating first label
miles = Label(text="Miles", font=("Times New Roman", 15, "bold"))
miles.grid(row=0,column=2)

#creating second label
is_equal_to = Label(text="is equal to", font=("Times New Roman", 15, "bold"))
is_equal_to.grid(row=1,column=0)

#creating third label, this one will have the function applied to it
num_km = Label(text="0", font=("Times New Roman", 15, "bold"))
num_km.grid(row=1, column=1)

def update_num_km():
    miles_entered = int(num_miles.get())
    miles_to_km = round(miles_entered * 1.6)
    num_km.config(text=str(miles_to_km))

#creating the fourth label
km = Label(text="Km", font=("Times New Roman", 15, "bold"))
km.grid(row=1, column=2)

#creating a button
calculate = Button(text="Calculate",  font=("Times New Roman", 15, "bold"))
calculate.config(width=15, command=update_num_km)
calculate.grid(row=2, column=1)



window.mainloop()