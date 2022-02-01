import tkinter

#Creating a window
window = tkinter.Tk()
window.title("Mile to Kilometer Project")
window.minsize(height=200,width=400)
window.config(padx=100,pady=25)

#Creating An Entry
input = tkinter.Entry(width=20)
input.grid(row=0,column=1)

#Creating Miles Label
miles = tkinter.Label(text="Miles")
miles.grid(row=0,column=2)
miles.config(padx=10)

#Function for converting miles to kilometer
def converter():
    my_miles = input.get()
    if my_miles != '':
        return label_1.config(text =f"is equal to    {round(1.609*float(my_miles),2)} Km")


#Button to calculate
calculate = tkinter.Button(text= "Calculate", command = converter)
calculate.grid(row=2,column=1,pady=10)

#Label
label_1 = tkinter.Label(text=f"is equal to    0 Km")
label_1.grid(row=3,column=1,pady=20)

window.mainloop()




