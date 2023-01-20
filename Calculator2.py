from tkinter import *

def btnClick(numbers):
       global operator
       operator=operator + str(numbers)
       text_Input.set(operator)

def btnClearDisplay():
       global operator
       operator=""
       text_Input.set("")

def btnEqualsInput():
       global operator
       sumup=str(eval(operator))
       text_Input.set(sumup)
       operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

Entry(cal, font=('arial', 16, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
      bg="light green", justify='right').grid(columnspan=4)

Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="7", command=lambda:btnClick(7),bg="light green").grid(row=1, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="8", command=lambda:btnClick(8), bg="light green").grid(row=1, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="9", command=lambda:btnClick(9),bg="light green").grid(row=1, column=2)
Division=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="/", command=lambda:btnClick("/"), bg="light green").grid(row=1, column=3)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="4", command=lambda:btnClick(4), bg="light green").grid(row=2, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="5", command=lambda:btnClick(5), bg="light green").grid(row=2, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="6", command=lambda:btnClick(6), bg="light green").grid(row=2, column=2)
Multiplication=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="*", command=lambda:btnClick("*"), bg="light green").grid(row=2, column=3)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="1", command=lambda:btnClick(1), bg="light green").grid(row=3, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="2", command=lambda:btnClick(2), bg="light green").grid(row=3, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="3", command=lambda:btnClick(3), bg="light green").grid(row=3, column=2)
Addition=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="+", command=lambda:btnClick("+"), bg="light green").grid(row=3, column=3)
Clear=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="C", command=btnClearDisplay, bg="light green").grid(row=4, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="0", command=lambda:btnClick(0), bg="light green").grid(row=4, column=1)
Equals=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="=", command=btnEqualsInput, bg="light green").grid(row=4, column=2)
Subtraction=Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
       text="-", command=lambda:btnClick("-"), bg="light green").grid(row=4, column=3)

cal.mainloop()
