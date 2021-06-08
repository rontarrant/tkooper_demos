from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		listbox_ = ListBox(self)
		remove_button = RemoveButton(self, listbox_)
		add_entry = AddEntry(self)
		add_button = AddButton(self, listbox_, add_entry)
		# layout
		listbox_.grid(column = 0, row = 0)
		listbox_.y_scrollbar.grid(column = 1, row = 0, sticky = (N, S)) # Without the sticky option, the thumb doesn't move.
		remove_button.grid(column = 0, row = 1)
		add_entry.grid(column = 0, row = 2)
		add_button.grid(column = 1, row = 2)

class ListBox(Listbox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.y_scrollbar = YScrollbar(parent)
		self.y_scrollbar.set_up(self)
		self.items = ['blue', 'red', 'yellow', 'orange', 'purple', 'green', 'brown', 'mauve', 'violet', 'black', 'white', 'teal', 'aqua', 'cerulean']
		self.items_var = StringVar(value = self.items)
		# configure
		self.config(listvariable = self.items_var, yscrollcommand = self.y_scrollbar.set)
		self.decorate_list()
		
	def decorate_list(self):
		for i in range(0, len(self.items), 2):
			self.itemconfigure(i, background = '#f0f0ff')
			
	def remove_item(self):
		indices = self.curselection()
		
		if len(indices) == 1:
			index = int(indices[0])
		
		print(f"Removed item #{index} which was: {self.items[index]}")
		self.items.remove(self.items[index])
		self.items_var.set(self.items)
		self.decorate_list()
		
	def add_item(self, item):
		self.items.append(item)
		self.items_var.set(self.items)
		self.decorate_list()
		self.see(len(self.items) - 1)
		
class YScrollbar(ttk.Scrollbar):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		self.configure(orient = VERTICAL)
		
	def set_up(self, buddy_widget):
		self.config(command = buddy_widget.yview)
	
class AddEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.string = StringVar()
		# configure
		self.config(textvariable = self.string)
		
	def clear(self):
		self.delete(0, 'end')
	
class AddButton(ttk.Button):
	def __init__(self, parent, listbox, entry):
		super().__init__(parent)
		# object attributes
		self.title_ = "Add Item"
		# configure
		self.config(text = self.title_, command = lambda: self.action(listbox, entry))
		
	def action(self, listbox, entry):
		listbox.add_item(entry.get())
		entry.clear()
		
class RemoveButton(ttk.Button):
	def __init__(self, parent, listbox):
		super().__init__(parent)
		# object attributes
		self.title_ = "Remove Item"
		# configure
		self.config(text = self.title_, command = lambda:self.action(listbox))

	def action(self, listbox):
		listbox.remove_item()

		
if __name__ == "__main__":
	main()
