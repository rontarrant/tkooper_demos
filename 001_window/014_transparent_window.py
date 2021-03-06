from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("A Simple Label")
		self.width = 260
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		self.wm_attributes('-alpha', 0.7)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		hello_label = SimpleLabel(self)
		# layout
		hello_label.grid(column = 0, row = 0)

class SimpleLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Definitely a Simple Label"
		self.width = len(self.text) # width is in characters
		self.photo = PhotoImage(file = "./images/example.png")
		# configure
		self.config(text = self.text, width = self.width)

'''
from tkinter import *

class HelloLabel(Label):
	def __init__(self, parent):
		super().__init__(parent)
		self.config(fg = "black", text = "Hello, World!")
		self.pack(ipadx = 20, ipady = 30, padx = (20, 30))

main = Tk()
photo = PhotoImage(file = "./example.png")
Label(main, image = photo, bg = 'grey').pack()
#your other label or button or ...
label = HelloLabel(main)
label['bg'] = label.master['bg']

main.wm_attributes("-transparentcolor", 'grey')
main.mainloop()
'''

if __name__ == "__main__":
	main()
