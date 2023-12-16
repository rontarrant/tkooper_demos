'''
after_idle() simply calls whatever method/function it's pointed at, handling arguments
as well, if necessary. Because there's no delay, it just does its business, but with
one caviat... updating the UI gets lost along the way. So, that has to be handled
by adding an extra line of code:

self.update_idletasks()

If this isn't done, the initial drawing of the UI is skipped and you can't even tell
if the application is running.
	
So, the bottom line is this: after() is less complex to use, even if by one bitty
little statement. If you wanna see how after_idle() differs, comment out the
self.update_idletasks() statement and run this script.
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
		
		self.update_idletasks()
		self.after_idle(self.tick)

if __name__ == "__main__":
	main()
