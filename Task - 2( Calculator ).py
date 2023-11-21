from tkinter import *
expression = "" 
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 
def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 
	except: 
		equation.set(" error ") 
		expression = "" 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
    
gui = Tk() 
gui.title("Calculator (CODSOFT TASK - 2)") 
gui.geometry("300x210") 

equation = StringVar() 

expression_field = Entry(gui, textvariable=equation, state=DISABLED).grid(columnspan=4, ipadx=80, pady=(5,5),padx=(5,5)) 

button1 = Button(gui, text=' 1 ', command=lambda: press(1), height=1, width=6).grid(row=3, column=0, pady=(5,5),padx=(5,5)) 
button2 = Button(gui, text=' 2 ', command=lambda: press(2), height=1, width=6).grid(row=3, column=1, pady=(5,5),padx=(5,5))
button3 = Button(gui, text=' 3 ', command=lambda: press(3), height=1, width=6).grid(row=3, column=2, pady=(5,5),padx=(5,5))
divide = Button(gui, text=' / ', command=lambda: press("/"), height=1, width=6).grid(row=3, column=3, pady=(5,5),padx=(5,5))

button4 = Button(gui, text=' 4 ', command=lambda: press(4), height=1, width=6).grid(row=2, column=0, pady=(5,5),padx=(5,5))
button5 = Button(gui, text=' 5 ', command=lambda: press(5), height=1, width=6).grid(row=2, column=1, pady=(5,5),padx=(5,5))
button6 = Button(gui, text=' 6 ', command=lambda: press(6), height=1, width=6).grid(row=2, column=2, pady=(5,5),padx=(5,5))
multiply = Button(gui, text=' * ', command=lambda: press("*"), height=1, width=6).grid(row=2, column=3, pady=(5,5),padx=(5,5))

button7 = Button(gui, text=' 7 ', command=lambda: press(7), height=1, width=6).grid(row=1, column=0, pady=(5,5),padx=(5,5))
button8 = Button(gui, text=' 8 ', command=lambda: press(8), height=1, width=6).grid(row=1, column=1, pady=(5,5),padx=(5,5))
button9 = Button(gui, text=' 9 ', command=lambda: press(9), height=1, width=6).grid(row=1, column=2, pady=(5,5),padx=(5,5))
plus = Button(gui, text=' + ', command=lambda: press("+"), height=1, width=6).grid(row=1, column=3, pady=(5,5),padx=(5,5))

Decimal= Button(gui, text='.', command=lambda: press('.'), height=1, width=6).grid(row=4, column=0, pady=(5,5),padx=(5,5))
button0 = Button(gui, text=' 0 ', command=lambda: press(0), height=1, width=6).grid(row=4, column=1, pady=(5,5),padx=(5,5))
clear = Button(gui, text='C', command=clear, height=1, width=6).grid(row=4, column=2, pady=(5,5),padx=(5,5))
minus = Button(gui, text=' - ', command=lambda: press("-"), height=1, width=6).grid(row=4, column=3, pady=(5,5),padx=(5,5))

equal = Button(gui, text=' = ', command=equalpress, height=1, width=37).grid(columnspan=4, pady=(5,5),padx=(5,5)) 

gui.mainloop()