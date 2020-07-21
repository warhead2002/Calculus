import tkinter as tk
from functools import partial
import sympy as sm
x,y,z=sm.symbols('x y z')
def integrate(label_result, n1, n2, n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    result = sm.integrate(num1,(x,num2,num3))
    label_result.config(text='Integration of the function is: %s '  %(result) )
    return
def diff(label_result, n1):
    num1 = (n1.get())
    result1 = sm.diff(num1,x)
    label_result.config(text='Differentiation of the function is: %s'  %( result1) )
    return



root = tk.Tk()
root.geometry('550x300')
root.title('Calculus Calculator')
root.configure(bg='blue')


number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()

labelTitle = tk.Label(root, text="Calculus Calculator", bg="red", font="Helvetica").grid(row=0, column=1)
labelNum1 = tk.Label(root, text="Enter the function", font="sans-serif").grid(row=3, column=0)
llimit = tk.Label(root, text="Enter the lower limit", font="sans-serif").grid(row=4, column=0)
ulimit = tk.Label(root, text="Enter the upper limit", font="sans-serif").grid(row=5, column=0)
labelResult = tk.Label(root, bg="grey", font=("arial",14))
labelResult.grid(row=10, column=1)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=3, column=1)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=4, column=1)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=5, column=1)

integrate = partial(integrate, labelResult, number1, number2, number3)
diff = partial(diff, labelResult, number1)

blank = tk.Label(root, text="", bg="blue").grid(row=8, column=0)
blank2 = tk.Label(root, text="", bg="blue").grid(row=2, column=0)
blank3 = tk.Label(root, text="", bg="blue").grid(row=6, column=0)

buttonCal = tk.Button(root, text="Integration", command=integrate,fg="grey",bg="black", font=("Times",12, "bold")).grid(row=7, column=0)
buttonCal = tk.Button(root, text="Differentiation", command=diff, fg="yellow",bg="black", font=("Times",12,"bold")).grid(row=7, column=1)



root.mainloop()
