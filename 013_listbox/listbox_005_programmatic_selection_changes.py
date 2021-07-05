'''
This demonstrates several features of Listboxes:
- Listbox.curselection() -- get the currently-selected item
- Listbox.selection_set() -- set selection by index
- Listbox.selection_clear() -- deselect an item by index
- Listbox.see() -- make sure the selected item is visible in the UI
- Listbox.selection_includes() -- see if a specfic index item is selected
'''
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		self.grid_propagate(False)
		self.title("Listbox Switch and Report")
		self.geometry("400x200")
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		listbox_ = ListBox_(self)
		report_label = ReportLabel(self)
		report_button = ReportButton(self, listbox_, report_label)
		# layout
		listbox_.grid(column = 0, row = 0)
		listbox_.y_scrollbar.grid(column = 1, row = 0, sticky = (N, S)) # Without the sticky option, the thumb doesn't move.
		report_button.grid(column = 2, row = 1)
		report_label.grid(column = 2, row = 2)

class ReportLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.original_report = "Nothing selected"
		# configure
		self.config(text = self.original_report)
	
class ListBox_(Listbox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.y_scrollbar = YScrollbar(parent)
		self.y_scrollbar.set_up(self)
		self.items = ['blue', 'red', 'yellow', 'orange', 'purple', 'green', 'brown', 'mauve', 'violet', 'black', 'white', 'teal', 'aqua', 'cerulean']
		self.items_var = StringVar(value = self.items)
		# configure
		self.config(listvariable = self.items_var, height = 5, yscrollcommand = self.y_scrollbar.set) # listbox is also scrollable using the MMB wheel

class YScrollbar(ttk.Scrollbar):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		self.configure(orient = VERTICAL)
		
	def set_up(self, buddy_widget):
		self.config(command = buddy_widget.yview)
	
class ReportButton(ttk.Button):
	def __init__(self, parent, reportee, reporter):
		super().__init__(parent)
		# object attributes
		self.title_ = "Change and Report"
		# configure
		self.config(text = self.title_, command = lambda:self.change_and_report(reportee, reporter))

	def change_and_report(self, reportee, reporter):
		'''
		Print out the item selected by the user. Then
		'''
		indices = reportee.curselection()
		message_part_one = ""

		if not indices:
			original_index = 0
			message_part_one = "You selected nothing"
		elif len(indices) == 1:
			original_index =  int(indices[0])
			message_part_one = f"You selected item #{original_index} which is: {reportee.items[original_index]}"

		if original_index == 0:
			message_part_one = f"You selected the first item in the list: {reportee.items[original_index]}"
			
		
		reportee.selection_clear(original_index) # unselect the currently-selected item
		
		# If the last item in the Listbox is selected, we need to make sure
		# the index does go out of range. BUT, because of the way Python handles
		# list indexing, if the first item is selected, it's okay to let the else 
		# statement kick in and take the index to -1.
		if original_index == 0:
			index = len(reportee.items) - 1
		else:
			index = original_index - 1

		reportee.selection_set(index)
		reportee.see(index) # also a demonstration of the see() method
		reporter.config(text = message_part_one + f",\nand it was switched to item #{index} which is: {reportee.items[index]}")

		print("\n")

		
if __name__ == "__main__":
	main()
