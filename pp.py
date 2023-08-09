from tkinter import *
from tkcalendar import *
aa_root=Tk()
def date_select():
    mydate=cal.get_date()
    date_select=Label(text=mydate)
    date_select.pack(padx=8,pady=8)
cal=Calendar(aa_root,setmode="day",date_pattern='dd/mm/yyyy')
cal.pack(padx=15,pady=15)
aa_root.title("Calendar")
aa_root.geometry("555x555")
aa_root.minsize(100,200)
frame=Frame(aa_root,borderwidth=5,bg="blue",relief="ridge")
frame.pack()

button=Button(frame,fg="blue",bg="grey",text="Select The Date",font="Times 11 bold",command=date_select)
button.pack()

aa_root.mainloop()