from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Checkbutton OOP")
		self.size = "200x300"
		# configure
		self.geometry(self.size)
		self.grid_propagate(False)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		parent_checkbutton = ParentCheckbutton(self)
		self.build_child_list(parent_checkbutton)
		# layout
		parent_checkbutton.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nw')
		row_ = 1
		print(parent_checkbutton.children)
		for childcheckbutton in parent_checkbutton.children:
			print(childcheckbutton)
			childcheckbutton.grid(row = row_, column = 0, padx = 10, pady = 10, sticky = 'se')
			row_ += 1

	def build_child_list(self, parent_checkbutton):
		child_names = ("Sub-option 1", "Sub-option 2", "Sub-option 3")
		
		for child_name in child_names:
			parent_checkbutton.children.append(ChildCheckbutton(self, parent_checkbutton, child_name))
			# indenting?

class ChildCheckbutton(ttk.Checkbutton):
	def __init__(self, parent, parent_checkbutton, name):
		super().__init__(parent)
		# object attributes
		self.var = IntVar()
		# configure
		self.config(text = name, onvalue = 1, offvalue = 0, variable = self.var)
		self.config(padding = (15, 0, 0, 0), command = lambda:self.update_(parent_checkbutton))
	
	def update_(self, parent_checkbutton):
		print(f"name: {self.cget('text')} - {self.var.get()} - state: {self.state()}")
		parent_checkbutton.update_()
			
class ParentCheckbutton(ttk.Checkbutton):
	def __init__(self, parent):
		super().__init__(parent)
		#object attributes
		self.text = "Option 1"
		self.var = IntVar()
		self.children = []
		# config
		self.config(text = self.text, onvalue = 1, offvalue = 0, variable = self.var, command = self.update_all)

	def update_all(self):
		if self.instate(['!selected']):
			for child in self.children:
				child.state(['!selected'])
		else:
			for child in self.children:
				child.state(['selected'])
		
	def update_(self):
		checked = 0

		for child in self.children:
			print(child.var.get())
			
			if child.instate(['selected']):
				checked += 1

		print(f"checked = {checked}")
		# are all children checked?
		if checked == len(self.children):
			print("setting state: selected")
			self.state(['!alternate']) # this must be cleared before any other state is set
			self.state(['selected'])
		# if not, is at least one child checked?
		elif checked > 0 & checked < len(self.children):
			print("setting state: alternate")
			self.state(['alternate'])
		# no children checked
		else:
			print("setting state: NOT selected")
			self.state(['!alternate'])
			self.state(['!selected'])

	
if __name__ == "__main__":
	main()
