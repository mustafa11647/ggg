from tkinter import*
from datetime import date
root=Tk()
root.title('getting started with widgets')
root.geometry('400x500')
#add widgets(label,entry,button)
lbl=Label(text="hey there!",fg="light green",bg="dark green",height=1,width=300)
name_lbl=Label(text="FULL NAME",bg="dark green")
name_entry=Entry()
def display():
    name=name_entry.get()
    Message="welcome to the app\ntodays date is: "
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="begin",command=display,height=1,bg="dark green",fg="green")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()












root.mainloop()

