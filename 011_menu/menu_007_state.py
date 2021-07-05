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
		self.add_radiobutton(label = "English", variable = self.current_language, value = "_english", command = self.set_language)
		self.add_radiobutton(label = "French", variable = self.current_language, value = "_french", command = self.set_language)
		self.add_radiobutton(label = "Lua", variable = self.current_language, value = "lua", command = self.set_language)
		self.add_radiobutton(label = "PHP", variable = self.current_language, value = "php", command = self.set_language)
		self.add_radiobutton(label = "Polish", variable = self.current_language, value = "_polish", command = self.set_language)
		self.add_radiobutton(label = "Python", variable = self.current_language, value = "python", command = self.set_language)
		
	def set_language(self):
		print(f"Current language is now set to: {self.current_language.get()}")

	def toggle_spoken_languages(self):
		menu_item_count = self.index(END)
		
		for i in range(menu_item_count + 1):
			value = self.entrycget(i, "value")
			# all spoken language values start with '_' so we can use
			# that as a filter to see which need to be disabled.
			if value[:1] == "_":
				if self.entrycget(i, "state") == 'disabled':
					self.entryconfigure(i, state = "normal")
				else:
					self.entryconfigure(i, state = "disabled")

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
		self.config(text = self.text, command = self.window.menubar.language_menu.toggle_spoken_languages)


if __name__ == "__main__":
	main()
