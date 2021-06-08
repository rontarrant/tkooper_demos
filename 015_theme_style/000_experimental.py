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

class MainFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Switch Button Style"
		# configure
		self.grid()
		self.config(labelanchor = 'nw', text = self.text)
		# populate
		theme_name_button = ThemeNameButton(self)
		theme_step_button = ThemeStepButton(self)
		# layout
		theme_name_button.grid(padx = 20, pady = 20)
		theme_step_button.grid(padx = 20, pady = 20)

class AppStyle(ttk.Style):
	def __init__(self):
		super().__init__()
		# class attributes
		self.themes = self.theme_names()
		self.theme_use('default')
		# configure derivative styles
		self.config_styles()

	def config_styles(self):
		self.configure("Go.TButton", background = '#12a31c', foreground = 'yellow', font = ('Times New Roman', 12, 'normal'))
		self.configure("Stop.TButton", background = 'red', foreground = 'yellow', compound = 'image')
		self.configure('TButton', font = ('Courier New', 12, 'bold', 'italic'), relief = 'sunken')
		self.configure("TButton", relief = 'raised', borderwidth = 5, bordercolor = 'red')
		self.map('Go.TButton',   background = [('active', '#12a31c')], foreground = [('active', 'black')])
		self.map("Stop.TButton", background = [('active', 'red')], foreground = [('pressed', 'blue'), ('active', 'black')])
		
class ThemeNameButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.style = AppStyle()
		self.text = ["GO!", "STOP!"]
		self.sub_styles = ['Go.TButton', 'Stop.TButton']
		# configure
		self.config(text = self.text[0], command = self.change_, style = self.sub_styles[0])

	def change_(self):
		if self.cget('style') == self.sub_styles[0]:
			self.config(text = self.text[1], style = self.sub_styles[1])
		else:
			self.config(text = self.text[0], style = self.sub_styles[0])
			
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
		self.style.config_styles() # set up styles for the new theme

	def set_theme_index(self):
		current_theme_name = self.style.theme_use()
		
		for name in self.theme_names:
			if name == current_theme_name:
				break
			else:
				self.index += 1


if __name__ == "__main__":
	main()
