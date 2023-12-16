'''
Assigning keyboard shortcuts to menu checkbuttons adds a dimension
of trickiness to actions that won't exist in standard menu buttons.
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
		self.bind('<Control_L><c>', self.menubar.edit_menu.copy_stuff)
		self.bind('<Control_L><x>', self.menubar.edit_menu.cut_stuff)
		self.bind('<Control_L><p>', self.menubar.edit_menu.paste_stuff)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		self.edit_menu = EditMenu(self, window)
		# attach menus
		self.add_cascade(menu = self.edit_menu, label = self.edit_menu.label_text)

class EditMenu(Menu):
	def __init__(self, menubar, window):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Edit"
		# menu items
		# populate
		self.add_command(label = "Copy", command = self.copy_stuff, accelerator = "(Ctrl-C)")
		self.add_command(label = "Cut", command = self.cut_stuff, accelerator = "(Ctrl-X)")
		self.add_command(label = "Paste", command = self.paste_stuff, accelerator = "(Ctrl-P)")

	def copy_stuff(self, event = None):
		print("Copying stuff...", event)
		self.pretty_print_event(event)
		
	def pretty_print_event(self, event):
		print("widget:", event.widget)
		print("state: ", event.state)
		print("char: ", event.char)
		print("num: ", event.num)
		print("keysym: ", event.keysym)
		print("keycode: ", event.keycode)
		print("x: ", event.x)
		print("y: ", event.y)
		print("width: ", event.width)
		print("height: ", event.height)
		print("send event: ", event.send_event)
		print("state: ", event.state)

	def cut_stuff(self, event = None):
		print("Cutting stuff.")

	def paste_stuff(self, event = None):
		print("Pasting stuff.")


if __name__ == "__main__":
	main()
