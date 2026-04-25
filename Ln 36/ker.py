from tkinter import *
from datetime import date
window=Tk()
window.title("Getting started with widgets")
window.geometry("400x300")
lbl=Label(text="Hey There!@#$%^",fg="white",bg="blue",height=1,width=300)
name_lbl=Label(text="Enter full name",bg="orange")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to Application! Todays date is :"
    greet="hello "+ name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="Begin",command=display,height=1,bg="light blue",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()
