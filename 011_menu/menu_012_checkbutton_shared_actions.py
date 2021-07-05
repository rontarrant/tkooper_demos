'''
Assigning keyboard shortcuts to menu checkbuttons adds a dimension
of trickiness to actions that won't exists when dealing with standard
menu buttons. When toggled by selecting the menu checkbutton itself,
the checkbutton's value toggles automatically. But when a keyboard 
shortcut is used, the toggle must be handled in the code.

The easiest way to do this is to check whether an event triggered the 
callback. If it was selected from the menu, the event will be unassigned
(event = None) but if triggered by a keyboard shortcut, the event 
will have an object assigned to it that looks like this:

<KeyPress event state = Control|Mod1 keysym = w keycode = 87 char = '\x17' x = 51 y = 40>

For clarity, the object can be laid out like this:
KeyPress event: # type of event
	state = Control | Mod1 # name of modifier key
	keysym = w # face value of key
	keycode = 87 # ASCII representing the key
	char = '\x17' # character ending the event sequence
	x = 51 # window coordinates of mouse pointer
	y = 40
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
		self.actions = Actions()
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)
		self.bind('<Control_L><w>', self.actions.set_word_wrap)
		self.bind('<Control_L><t>', self.actions.set_tabs)
		self.bind('<Control_L><l>', self.actions.set_line_numbers)

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
		self.actions = window.actions
		# menu items
		# populate
		self.add_checkbutton(label = "Word Wrap", variable = self.actions.wrap, onvalue = True, offvalue = False, command = self.actions.set_word_wrap, accelerator = "(Ctrl-W)")
		self.add_checkbutton(label = "Show Tabs", variable = self.actions.tabs, onvalue = True, offvalue = False, command = self.actions.set_tabs, accelerator = "(Ctrl-T)")
		self.add_checkbutton(label = "Line Numbers", variable = self.actions.line_numbers, onvalue = True, offvalue = False, command = self.actions.set_line_numbers, accelerator = "(Ctrl-L)")

class Actions():
	def __init__(self):
		self.wrap = BooleanVar()
		self.tabs = BooleanVar()
		self.line_numbers = BooleanVar()
		self.settings_menu = None
		
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
