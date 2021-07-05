# To accommodate the user typing in a response, external action needs to be taken
# by some other widget, in this case, a ttk.Button.
# The Combobox can report on anything selected from the supplied list, but
# another widget must be present to deal with a user-typed response.
# There are two ways to handle this:
#	- supply a widget (such as a Button) to go in and grab the user response, or
#	- add another widget to which focus can be moved if the user hits the Tab key.
# In the case of the latter, the Combobox can then hand off the user-typed response
# via the validation process discussed in some of the ttk.Entry demos. 
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Simple Entry"
		# configure
		self.title(self.title_text)
		self.config(width = 270, height = 100)
		self.grid_propagate(False) # otherwise, window has no size at all
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		thing_combobox = DynamicCombobox(self)
		action_button = ActionButton(self, thing_combobox)
		# layout
		thing_combobox.grid(padx = 10, pady = 10)
		action_button.grid(padx = 10, pady = 10)

class DynamicCombobox(ttk.Combobox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.value_list = ['something', 'something else', 'another thing', 'and finally']
		self.var = StringVar()
		# configure
		self.config(textvariable = self.var, values = self.value_list)
		self.bind('<<ComboboxSelected>>', self.report) # note the double chevrons

	def add_user_input(self):
		'''
		Takes whatever the user has typed into the built-in Entry and adds it to the list of choices
		for the Combobox.
		'''
		if self.current() == -1:
			print(f"The user typed: {self.get()}")
			self.value_list.append(self.get())
			self.config(values = self.value_list) # the updated list needs to be reattached
			self.set("") # clear the Combobox's Entry

	def report(self, event): # the event argument needs to be here, even though it's not enlightening - it's always the set (x = 0, y = 0)
		'''
		Shows the values passed in by the event argument.
		'''
		print(f"event: {event}\nuser choice: {self.var.get()}")

class ActionButton(ttk.Button):
	def __init__(self, parent, paired_widget):
		super().__init__(parent)
		# object attributes
		self.buddy_widget = paired_widget
		self.text = "Take Action"
		self.message = "User selection: "
		# configure
		self.config(text = self.text, command = self.take_action)

	def take_action(self):
		print(f"{self.message} {self.buddy_widget.get()}")
		self.buddy_widget.add_user_input()

if __name__ == "__main__":
	main()
