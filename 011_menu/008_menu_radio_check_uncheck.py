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
		self.mainframe = MainFrame(self)
		# configure
		self.config(menu = self.menubar)
		

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		self.language_menu = LanguageMenu(self)
		# attach menus
		self.add_cascade(menu = self.language_menu, label = self.language_menu.label_text)

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
		self.add_radiobutton(label = "PHP", variable = self.current_language, value = "php", command = self.set_language)
		self.add_radiobutton(label = "Python", variable = self.current_language, value = "python", command = self.set_language)
		
	def set_language(self):
		print(f"Current language is now set to: {self.current_language.get()}")

	def check_previous_item(self):
		menu_item_count = self.index(END)
		
		# find the radiobutton that's checked
		for i in range(menu_item_count + 1):
			value = self.entrycget(i, "value")

			# if we find an item checked...
			if self.current_language.get() == value:
				break
				
		# if we're on the zeroth item...
		if (i - 1) < 0:
			# wrap around to the end of the list of items
			self.current_language.set(self.entrycget(menu_item_count, "value"))
		# we AREN'T on the zeroth item, so check the item before the current one
		else:
			# check the item before the current one
			#(which automatically unchecks the current item)
			self.current_language.set(self.entrycget(i - 1, "value"))

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hide_spoken_button = ToggleSpokenButton(self)
		# layout
		hide_spoken_button.grid()

class ToggleSpokenButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Toggle Spoken Languages"
		self.window = self.winfo_toplevel()
		# configure
		self.config(text = self.text, command = self.window.menubar.language_menu.check_previous_item)


if __name__ == "__main__":
	main()
