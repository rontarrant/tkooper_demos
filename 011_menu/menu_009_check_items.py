# Menus are handled a bit differently than other widgets.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.option_add('*tearOff', FALSE) # must be set BEFORE any menus are created
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		language_menu = LanguageMenu(self)
		# attach menus
		self.add_cascade(menu = language_menu, label = language_menu.label_text)

class LanguageMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Settings"
		self.wrap = BooleanVar()
		self.tabs = BooleanVar()
		self.line_numbers = BooleanVar()
		# menu items
		# populate
		self.add_checkbutton(label = "Word Wrap", variable = self.wrap, onvalue = True, offvalue = False, command = self.set_word_wrap)
		self.add_checkbutton(label = "Show Tabs", variable = self.tabs, onvalue = True, offvalue = False, command = self.set_tabs)
		self.add_checkbutton(label = "Line Numbers", variable = self.line_numbers, onvalue = True, offvalue = False, command = self.set_line_numbers)

	def set_word_wrap(self):
		on_off = self.wrap.get()
		
		if on_off == True:
			print("Word wrap is on.")
		else:
			print("Word wrap is off.")

	def set_tabs(self):
		on_off = self.tabs.get()
		
		if on_off == True:
			print("Tabs are now showing.")
		else:
			print("Tabs are now hidden.")

	def set_line_numbers(self):
		on_off = self.line_numbers.get()
		
		if on_off == True:
			print("Lines numbers: on.")
		else:
			print("Line numbers: off.")


if __name__ == "__main__":
	main()
