from tkinter import *

def sum_nums(event):
    num1 = int(num_1.get())
    num2 = int(num_2.get())
    sum_ = num1 + num2

    total.delete(0, "end")
    total.insert(0, sum_)
    
root = Tk()

num_1 = Entry(root) # First entry num 1
num_1.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT) # label to sum

num_2 = Entry(root) # the second entry
num_2.pack(side=LEFT)

equal_but = Button(root, text="=")
equal_but.bind("<Button-1>", sum_nums) # Button 1 press event executes the sum_nums functions
equal_but.pack(side=LEFT)

total = Entry(root) # an entry / input field for the total where we recive the sum of the operation
total.pack(side=LEFT)

root.mainloop()
