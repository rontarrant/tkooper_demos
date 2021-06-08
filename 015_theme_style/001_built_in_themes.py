from tkinter import *
from tkinter import ttk
from tkinter import font

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Theme & Style")
		# configure
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		northwest_labelframe = NWFrame(self)
		# layout
		northwest_labelframe.grid(row = 0, column = 0, padx = 10, pady = 10)

class NWFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Theme Explorer"
		# configure
		self.grid()
		self.config(labelanchor = 'nw', text = self.text)
		# populate
		first_label = StringLabel(self, "Some Label Text")
		theme_name_button = ThemeNameButton(self)
		theme_in_use_button = ThemeInUseButton(self)
		theme_step_button = ThemeStepButton(self)
		# layout
		first_label.grid(padx = 20, pady = 20)
		theme_name_button.grid(padx = 20, pady = 20)
		theme_in_use_button.grid(padx = 20, pady = 20)
		theme_step_button.grid(padx = 20, pady = 20)

class AppStyle(ttk.Style):
	def __init__(self):
		super().__init__()
		# class attributes
		self.themes = self.theme_names()
		self.theme_use('default')
		# configure
		
class StringLabel(ttk.Label):	
	def __init__(self, parent, text_):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(text = text_)

class ThemeNameButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Print Theme Names"
		self.style = AppStyle()
		# configure
		self.config(text = self.text, command = self.print_theme_names)

	def print_theme_names(self):
		for theme in self.style.theme_names():
			print(f"{theme}") # list available styles

class ThemeInUseButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Current Theme"
		self.style = AppStyle()
		# configure
		self.config(text = self.text, command = self.print_theme_in_use)

	def print_theme_in_use(self):
		print(f"current theme: {self.style.theme_use()}") # the theme that's in use now

class ThemeStepButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Next Theme"
		self.style = AppStyle()
		self.theme_names = self.style.theme_names()
		self.index = 0
		# configure
		self.set_theme_index()
		self.config(text = self.text, command = self.next_theme)

	def next_theme(self):
		self.index += 1

		if self.index > len(self.theme_names) - 1:
			self.index = 0

		print(f"new theme is: {self.theme_names[self.index]}")
		self.style.theme_use(self.theme_names[self.index]) # change theme

	def set_theme_index(self):
		current_theme_name = self.style.theme_use()
		
		for name in self.theme_names:
			if name == current_theme_name:
				break
			else:
				self.index += 1

if __name__ == "__main__":
	main()
