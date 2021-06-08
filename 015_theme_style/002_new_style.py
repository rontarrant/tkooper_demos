# Themes and Styles exist outside the hierarchy of widgets.
# Together they outline a plan for decorating widgets.
# To get the most complete control possible over a style, several things need to be done:
#	- define a style as a class,
#	- pick an existing theme to use,
#	- configure a derivative style based on an existing style, and
#	- map the new style to a widget.
# It's not known at this point if this gives 100% control over a derived style, but it's as close as I've come so far.
# A style item setting (ex. relief = 'raised') can be set for all widgets of a type (ex: TButton) and then overridden
# for a derived style (ex. Blue.TButton, relief = 'sunken').
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
		# configure derivative styles
		self.configure("Blue.TButton", background = '#0000ff', foreground = 'yellow', font = ('Times New Roman', 12, 'normal'))
		self.configure("Orange.TButton", background = 'orange', foreground = 'purple', font = ('Courier New', 12, 'bold', 'italic'), relief = 'sunken')
		self.configure("TButton", relief = 'raised')
		self.map('TButton', relief = [('pressed', 'sunken')])
		self.map('Blue.TButton',   background = [('active', '#00ff00')], foreground = [('active', 'purple')])
		self.map("Orange.TButton", background = [('active', 'white')], foreground = [('active', 'black')])
		
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
		self.style = AppStyle()
		self.text = "Print Theme Names"
		# configure
		self.config(text = self.text, command = self.print_theme_names, style = 'Blue.TButton')

	def print_theme_names(self):
		for theme in self.style.theme_names():
			print(theme) # list available styles
		
		#print(self.style.layout('TButton'))
		print(f"This button's Style: {self.winfo_class()}")

		if self.style.theme_use() == 'default':
			print(f"This button's sub-style: {self.configure()['style'][4]}") # NOTE: rewrite to reflect when sub-style NOT in use
		else:
			print("This button has no sub-style when dressed in this theme.")
			
		print(f"List of configurable options:")
		
		for option_ in self.configure():
			print(f"\t{option_}")

class ThemeInUseButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.style = AppStyle()
		self.text = "Current Theme"
		# configure
		self.config(text = self.text, command = self.print_theme_in_use)

	def print_theme_in_use(self):
		print(f"\nTheme in use: {self.style.theme_use()}") # the theme that's in use now
		print(f"This button's Style: {self.winfo_class()}")

		print("This button never has a sub-style because it was never given one.")

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
		self.config(text = self.text, command = self.next_theme, style = 'Orange.TButton')

	def next_theme(self):
		self.index += 1

		if self.index > len(self.theme_names) - 1:
			self.index = 0

		print(f"changing theme... new theme is: {self.theme_names[self.index]}")
		self.style.theme_use(self.theme_names[self.index]) # change theme
		print(f"This button's Style: {self.winfo_class()}")
		
		if self.style.theme_use() == 'default':
			print(f"This button's sub-style: {self.configure()['style'][4]}") # NOTE: rewrite to reflect when sub-style NOT in use
		else:
			print("This button has no sub-style when dressed in this theme.")

	def print_theme_in_use(self):
		print(self.style.theme_use())

	def set_theme_index(self):
		current_theme_name = self.style.theme_use()
		
		for name in self.theme_names:
			if name == current_theme_name:
				break
			else:
				self.index += 1
		
		print(self.index)


if __name__ == "__main__":
	main()
