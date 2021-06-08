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
		self.label_text = "Language"
		self.current_language = StringVar()
		# menu items
		# populate
		self.add_radiobutton(label = "C", variable = self.current_language, value = "c", command = self.set_language)
		self.add_radiobutton(label = "C++", variable = self.current_language, value = "c_plus_plus", command = self.set_language)
		self.add_radiobutton(label = "D", variable = self.current_language, value = "d", command = self.set_language)
		self.add_radiobutton(label = "Lua", variable = self.current_language, value = "lua", command = self.set_language)
		self.add_radiobutton(label = "Python", variable = self.current_language, value = "python", command = self.set_language)

	def set_language(self):
		print(f"Current language is now set to: {self.current_language.get()}")


if __name__ == "__main__":
	main()
