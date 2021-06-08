from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.two_seconds = 2000
		self.callable = print
		self.args = ('Hello', 'delayed', 'World')
		self.after(self.two_seconds, self.callable, self.args[0], self.args[1], self.args[2])

if __name__ == "__main__":
	main()
