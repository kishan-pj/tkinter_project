from _ast import Lambda
from tkinter import*

root=Tk()

# defining title of the project
root.title("Calculator")
e = Entry(root, width=50, borderwidth=10,bg="black",fg="white")
e.grid(row=0, column=0, columnspan=20, padx=35, pady=20 )

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num=int(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number =e.get()
    global f_num
    global math
    math = "multiplication"
    f_num=int(first_number)
    e.delete(0, END)

def button_division():
    first_number =e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)



def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math=="addition":
        e.insert(0,f_num + int(second_number))

    if math=="subtraction":
        e.insert(0,f_num-int(second_number))

    if math=="multiplication":
        e.insert(0,f_num*int(second_number))

    if math=="division":
        e.insert(0,f_num/int(second_number))


# Defining the Buttons
button_1 = Button(root, text = "1", padx = 44, pady = 20, command = lambda : button_click(1),bg="blue",fg="black")
button_2 = Button(root, text = "2", padx = 44, pady = 20, command = lambda : button_click(2),bg="blue",fg="black")
button_3 = Button(root, text = "3", padx = 44, pady = 20, command = lambda : button_click(3),bg="blue",fg="black")
button_4 = Button(root, text = "4", padx = 44, pady = 20, command = lambda : button_click(4),bg="blue",fg="black")
button_5 = Button(root, text = "5", padx = 44, pady = 20, command = lambda : button_click(5),bg="blue",fg="black")
button_6 = Button(root, text = "6", padx = 44, pady =20, command = lambda : button_click(6),bg="blue",fg="black")
button_7 = Button(root, text = "7", padx = 44, pady = 20, command = lambda : button_click(7),bg="blue",fg="black")
button_8 = Button(root, text = "8", padx = 44, pady = 20, command = lambda : button_click(8),bg="blue",fg="black")
button_9 = Button(root, text = "9", padx = 44, pady = 20, command = lambda : button_click(9),bg="blue",fg="black")
button_0 = Button(root, text = "0", padx = 44, pady = 20, command = lambda : button_click(0),bg="blue",fg="black")
button_addition = Button(root, text = "+", padx = 44, pady = 20, command = button_addition,bg="green",fg="black")
button_equal = Button(root, text = "=", padx = 44, pady =20, command = button_equal,bg="black",fg="white")
button_clear = Button(root, text = "Clear", padx =34, pady = 20, command = button_clear,bg="black",fg="white")
button_subtraction = Button(root,text = "-",padx = 44, pady = 20,command = button_subtraction,bg="green",fg="black")
button_multiplication = Button(root,text ="*",padx = 44, pady = 20, command = button_multiplication,bg="green",fg="black")
button_division = Button(root, text = "/",padx= 44, pady = 20, command = button_division,bg="green",fg="black",)


# Putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtraction.grid(row=3,column=3)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiplication.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1, column=2)
button_division.grid(row=1,column=3)

button_0.grid(row=4,column=2)
button_addition.grid(row=4,column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=1)


root.mainloop()