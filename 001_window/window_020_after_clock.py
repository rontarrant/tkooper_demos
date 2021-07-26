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
import time

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
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		# populate
		clock_label = ClockLabel(self)
		# layout
		clock_label.grid()

class ClockLabel(Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.curtime = ''
		# configure
		self.config(text = self.curtime)
		self.tick()

	def tick(self):
		newtime = time.strftime('%H:%M:%S')
		
		if newtime != self.curtime:
			self.curtime = newtime
			self.config(text = self.curtime)
			
		self.after(200, self.tick)

if __name__ == "__main__":
	main()
