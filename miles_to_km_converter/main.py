from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

input = Entry(width = 10)
input.grid(column=1,row=0)

label2 = Label(text="is equal to ")
label2.grid(column=0,row=1)

answer = Label()
answer.grid(column=1,row=1)

km = Label(text="Km")
km.grid(column=2,row=1)


def km_converter():
    data= float(input.get())
    kmc = round(data * 1.609)
    answer.config(text=f"{  kmc}")


button = Button(text="Calculate", command=km_converter)
button.grid(column=1,row=2)

window.mainloop()