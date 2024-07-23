from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Example")
window.minsize(width=500,height=300)


# Lable
lable  = Label(text="This is Old text",font=("Arial", 24, "bold"))
lable.config(text="This is new Text")
lable.pack()

def action():
    print("Do something")

#Button
button = Button(text="Click Me", command=action)
button.config(width=10)
button.pack()

#Entries
entry = Entry(width=30)
entry.insert(END,string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5,width=30)
#puts cursor in text box
text.focus()
text.insert(END,"Example of Multi line text entry")
print(text.get("1.0",END))
text.pack()

#Spin box

def spinbox_get():
    print(spinbox.get())
    
spinbox = Spinbox(from_=0,to=10,width=5 ,command=spinbox_get)
spinbox.pack()


#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()