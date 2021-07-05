from tkinter import *
from tkinter import ttk
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.option_add('*tearOff', FALSE) # must be set BEFORE any menus are created
		self.actions = Actions(self)
		self.popup_menu = PopUpMenu(self)
		# configure
		self.bind('<Control_L><c>', self.actions.copy_stuff)
		self.bind('<Control_L><x>', self.actions.cut_stuff)
		self.bind('<Control_L><p>', self.actions.paste_stuff)
		self.bind("<Button-3>", self.popup)
		# populate
		mainframe = MainFrame(self)
		
	def popup(self, event):
		try:
			self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
		finally:
			self.popup_menu.grab_release()

class PopUpMenu(Menu):
	def __init__(self, window):
		super().__init__()
		# object attributes
		self.label_text = "Edit"
		self.actions = window.actions
		# populate
		self.add_command(label = "Copy", command = self.actions.copy_stuff, accelerator = "(Ctrl-C)")
		self.add_command(label = "Cut", command = self.actions.cut_stuff, accelerator = "(Ctrl-X)")
		self.add_command(label = "Paste", command = self.actions.paste_stuff, accelerator = "(Ctrl-P)")

class Actions():
	def __init__(self, window):
		self.window = window

	def copy_stuff(self, event = None):
		self.window.focus_get().event_generate("<<Copy>>")
		print("Copying stuff.")

	def cut_stuff(self, event = None):
		self.window.focus_get().event_generate("<<Cut>>")
		print("Cutting stuff.")

	def paste_stuff(self, event = None):
		self.window.focus_get().event_generate("<<Paste>>")
		print("Pasting stuff.")

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		entry_one = StringEntry(self)
		entry_two = StringEntry(self)
		# layout
		entry_one.grid()
		entry_two.grid()

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.string = StringVar()
		# configure
		self.config(textvariable = self.string)
		self.bind('<Tab>', self.report)
		
	def report(self, event): # two ways to fetch the Entry contents
		print(self.get())
		print(self.string.get())


if __name__ == "__main__":
	main()
