'''
after() sets an amount of time to wait before calling the designated method/function.
Unlike sleep(), it doesn't lock up the application while waiting for the designated
time to pass.

If called recursively - the calling method/function containing after() is, itself,
called by after() - each time through the recursion, after() simply waits again
before re-calling the method/function. There's no delay in handling idle tasks.
'''
from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 290
		self.height = 200
		self.title_text = "Report After 1 Second"
		# configure
		self.after(1000, self.report)
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		
	def report(self):
		print("Reporting after 1000 ms.")

if __name__ == "__main__":
	main()
