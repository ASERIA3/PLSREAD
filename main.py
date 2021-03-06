import tkinter
from tkinter import *

expression = ""

def press(num):
	global expression

	expression = expression + str(num)

	equation.set(expression)


# Function to evaluate the final expression.
def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:
		equation.set(" error ")
		expression = ""

# Functions of text entry box.
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver/GUI code
if __name__ == "__main__":
	# creating a GUI window.
	gui = Tk()

	# setting the background colour of GUI window.
	gui.configure(background="light blue")

	# setting the title of GUI window.
	gui.title("Calculator")

	# setting the configuration of GUI window.
	gui.geometry("280x150")

	# StringVar() is the variable class then we create an instance of this class.
	equation = StringVar()

	# create the text entry box for showing the expression.
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing the widgets at respective position in table like structure.
	expression_field.grid(columnspan=4, ipadx=80, ipady=10)

	# create a Buttons and place at a particularlocation inside the root window when user press the button, the command or function affiliated to that button is executed.
	button1 = Button(gui, text=' 1 ', fg='black', bg='white',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=3, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='white',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=3, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='white',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=3, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='white',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=4, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='white',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=4, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='white',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=4, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='white',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=5, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='white',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=5, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='white',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=5, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='white',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=6, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='white',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=3, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='white',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=4, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='white',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=5, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='white',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=6, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='white',
				command=equalpress, height=1, width=7)
	equal.grid(row=6, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='white',
				command=clear, height=1, width=7)
	clear.grid(row=6, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='white',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=7, column=0)

	Reminder= Button(gui, text='WARNING', fg='black', bg='white',
					command=lambda: press('THIS IS NOT A SCIENTIFIC CALCULATOR'), height=1, width=7)
	Reminder.grid(row=7, column=1)

	#HEHEHE
	Present= Button(gui, text='GIFT', fg='red', bg='black',
					command=lambda: press('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height=1, width=7)
	Present.grid(row=7, column=2)

	import tkinter as hehe
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = hehe.Tk()
lbl = hehe.Label(root, text=r"https://www.youtube.com/watch?v=yPYZpwSpKmA", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()
	
# start the GUI
gui.mainloop()
