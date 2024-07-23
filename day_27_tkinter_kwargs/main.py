from tkinter import *


def button_clicked(input):
    print("I got clicked")
    # new_text = input.get()
    my_label.config(text=input)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=1,column=1)
my_label.config(padx=25,pady=25)
# Button
button1 = Button(text="Click me", command=lambda: button_clicked(input.get()))
button1.grid(row=2,column=2)

button2 = Button(text="submit", command=lambda: button_clicked(input.get()))
button2.grid(row=1,column=3)

# Entry
input = Entry(width=15)
input.grid(row=3,column=4)
input.get()

window.mainloop()