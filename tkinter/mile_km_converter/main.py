from tkinter import *

window = Tk()
window.title("Mile to KM Coverter")
# window.minsize(width=600,height=400)
window.config(padx=20,pady=20)


def get_lable(text,row_num=0,column_num=0):
    my_label1 = Label(text=text,font=("Arial", 14, "bold"))
    my_label1.grid(row=row_num,column=column_num)


get_lable(text="Is Equal to:",row_num=2,column_num=1)
get_lable(text="Miles",row_num=1,column_num=3)
get_lable(text="Km",row_num=2,column_num=3)

miles_input = Entry(width=25)
miles_input.focus()
miles_input.grid(row=1,column=2)
miles_input.get()

km_result = Label(text="0",font=("Arial", 14, "bold"))
km_result.grid(row=2,column=2)

# input2 = Entry(width=25)
# input2.grid(row=2,column=2)
# input2.get()


def mile_km_converter():
    mile = miles_input.get()
    km = 1.60934*float(mile)
    km_result.config(text=f"{km}")
    

button = Button(text= "Calulate",command=mile_km_converter)
button.grid(row=3,column=2)
# button.config(padx=25,pady=25)

window.mainloop()