from tkinter import *

window = Tk()

window.title("Getting Started with Widgets")
window.geometry("400x300")

first_num = Label(text="Enter first number: ",
              fg="white",
              bg="light blue",
              font=("Arial Bold", 16))
first_num_entry = Entry()

second_num = Label(text="Enter second number: ",
              fg="white",
              bg="light blue",
              font=("Arial Bold", 16))
second_num_entry = Entry()

def display():
  f_n = first_num_entry.get()
  s_n = second_num_entry.get()
  msg = "The product of the two number is: "
  product = int(f_n) * int(s_n)
  
  text_box.insert(END, msg)
  text_box.insert(END, product)


text_box = Text(height=3)
btn = Button(text="Click me",
             command=display,
             height=1,
             bg="light blue",
             fg="white")

first_num.pack()
second_num.pack()
first_num_entry.pack()
second_num_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()
