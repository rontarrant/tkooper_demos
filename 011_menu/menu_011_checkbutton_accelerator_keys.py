'''
Assigning keyboard shortcuts to menu checkbuttons adds a dimension
of trickiness to actions that won't exists in standard menu buttons.
When toggled by selecting the menu checkbutton, the checkbutton's
value toggles automatically. But when a keyboard shortcut is used,
the toggle must be handled in the code. The easiest way to do this
is to check the event that triggered the callback. If it was selected
from the menu, there won't be an event (event = None) but if triggered
by a keyboard shortcut, the event will be a full-blown actual event.
'''
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
		self.bind('<Control_L><w>', self.menubar.settings_menu.set_word_wrap)
		self.bind('<Control_L><t>', self.menubar.settings_menu.set_tabs)
		self.bind('<Control_L><l>', self.menubar.settings_menu.set_line_numbers)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		self.settings_menu = SettingsMenu(self, window)
		# attach menus
		self.add_cascade(menu = self.settings_menu, label = self.settings_menu.label_text)

class SettingsMenu(Menu):
	def __init__(self, menubar, window):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Settings"
		self.wrap = BooleanVar()
		self.tabs = BooleanVar()
		self.line_numbers = BooleanVar()
		# populate
		self.add_checkbutton(label = "Word Wrap", variable = self.wrap, onvalue = True, offvalue = False, command = self.set_word_wrap, accelerator = "(Ctrl-W)")
		self.add_checkbutton(label = "Show Tabs", variable = self.tabs, onvalue = True, offvalue = False, command = self.set_tabs, accelerator = "(Ctrl-T)")
		self.add_checkbutton(label = "Line Numbers", variable = self.line_numbers, onvalue = True, offvalue = False, command = self.set_line_numbers, accelerator = "(Ctrl-L)")

	def set_word_wrap(self, event = None):
		if event != None: # triggered by keyboard shortcut
			if self.wrap.get() == True:
				self.wrap.set(False)
			else:
				self.wrap.set(True)
		
		if self.wrap.get() == True:
			print("Word wrap is on.")
		else:
			print("Word wrap is off.")

	def set_tabs(self, event = None):
		if event != None: # triggered by keyboard shortcut
			if self.tabs.get() == True:
				self.tabs.set(False)
			else:
				self.tabs.set(True)
		
		if self.tabs.get() == True:
			print("Tabs are now showing.")
		else:
			print("Tabs are now hidden.")

	def set_line_numbers(self, event = None):
		if event != None: # triggered by keyboard shortcut
			if self.line_numbers.get() == True:
				self.line_numbers.set(False)
			else:
				self.line_numbers.set(True)
		
		if self.line_numbers.get() == True:
			print("Lines numbers: on.")
		else:
			print("Line numbers: off.")


if __name__ == "__main__":
	main()
