'''
after() sets an amount of time to wait before calling the designated method/function.
Unlike sleep(), it doesn't lock up the application while waiting for the designated
time to pass.

If called recursively - the calling method/function containing after() is, itself,
called by after() - each time through the recursion, after() simply waits again
before re-calling the method/function. There's no delay in handling idle tasks.
'''
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.delay = 5000
		self.callable = print
		self.args = ('Hello', 'delayed', 'World')
		self.after(self.delay, self.callable, self.args[0], self.args[1], self.args[2])

if __name__ == "__main__":
	main()
