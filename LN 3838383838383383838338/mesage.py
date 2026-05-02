from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
def msg():
    messagebox.showwarning("Alert","Stop!virus")
btn=Button(window,text="Scan for virus",command=msg)
btn.place(x=40,y=40)
window.mainloop()