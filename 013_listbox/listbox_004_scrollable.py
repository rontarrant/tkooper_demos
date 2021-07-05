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
		listbox_ = ListBox_(self)
		report_button = ReportButton(self, listbox_)
		# layout
		listbox_.grid(column = 0, row = 0)
		listbox_.y_scrollbar.grid(column = 1, row = 0, sticky = (N, S)) # Without the sticky option, the thumb doesn't move.
		report_button.grid(column = 0, row = 1)

class ListBox_(Listbox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.y_scrollbar = YScrollbar(parent)
		self.y_scrollbar.set_up(self)
		self.items = ['blue', 'red', 'yellow', 'orange', 'purple', 'green', 'brown', 'mauve', 'violet', 'black', 'white', 'teal', 'aqua', 'cerulean']
		self.items_var = StringVar(value = self.items)
		# configure
		self.config(listvariable = self.items_var, height = 5, yscrollcommand = self.y_scrollbar.set)
		
class YScrollbar(ttk.Scrollbar):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		self.configure(orient = VERTICAL)
		
	def set_up(self, buddy_widget):
		self.config(command = buddy_widget.yview)
	
class ReportButton(ttk.Button):
	def __init__(self, parent, reportee):
		super().__init__(parent)
		# object attributes
		self.title_ = "Report"
		# configure
		self.config(text = self.title_, command = lambda:self.report(reportee))

	def report(self, reportee):
		for item in reportee.curselection():
			print(reportee.items[item])

		
if __name__ == "__main__":
	main()
