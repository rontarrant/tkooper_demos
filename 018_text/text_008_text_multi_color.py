from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Text Display Simple")
		# configure
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		# populate
		mainframe = MainFrame(self)

class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid(column = 0, row = 0, sticky = (N, E, W, S))
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		# populate
		text_display = TextDisplay(self)
		text_scrollbar = TextScrollbar(self, text_display)
		# layout
		text_display.grid(column = 0, row = 0, sticky = (N, E, W, S))
		text_scrollbar.grid(column = 1, row = 0, sticky = (N, S))

class TextDisplay(Text):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.width = 40 # characters
		self.height = 10 # character rows
		self.wrap = "word"
		# configure
		self.config(width = self.width, height = self.height, wrap = self.wrap)
		self.config(fg = "blue")
		print(self.tag_configure("action"))

class TextScrollbar(Scrollbar):
	def __init__(self, parent, widget):
		super().__init__(parent)
		# object attributes
		self.orientation = VERTICAL
		# configure
		self.config(command = widget.yview) # scrollbar to widget communication
		widget.config(yscrollcommand = self.set) # widget to scrollbar communications


if __name__ == "__main__":
	main()


'''
# Notes
- character.lmargin1 : use for character name
- character.lmargin2 : Use for Extensions

- need to know which element the cursor is in
- need a list (array? dictionary?) of elements
	- font
	- font colour
	- left margin
	- right margin
	- width (in characters)
	- 
- need a list (array? dictionary?) of element sections in the script
	- beginning and end of each element section
	- 

# flow control for special key events while typing

if <Enter>:
	if current_tag == "scene":
		pass
	elif current_tag == "action":
		pass
	elif current_tag == "character":
		pass
	elif current_tag == "dialogue":
		pass
	elif current_tag == "parenthetical":
		pass
	elif current_tag == "transition":
		pass
	elif current_tag == "extention":
		pass
	elif current_tag == "subheader":
		pass
elif <Tab>
	if current_tag == "scene":
		pass
	elif current_tag == "action":
		pass
	elif current_tag == "character":
		pass
	elif current_tag == "dialogue":
		pass
	elif current_tag == "parenthetical":
		pass
	elif current_tag == "transition":
		pass
	elif current_tag == "extention":
		pass
	elif current_tag == "subheader":
		pass
elif <Shift-Tab>
	if current_tag == "scene":
		pass
	elif current_tag == "action":
		pass
	elif current_tag == "character":
		pass
	elif current_tag == "dialogue":
		pass
	elif current_tag == "parenthetical":
		pass
	elif current_tag == "transition":
		pass
	elif current_tag == "extention":
		pass
	elif current_tag == "subheader":
		pass

# outlines for element tags

top_line:
	left margin: 1.5"
	right margin:
		7.5" from left,
		1" from right
	width: 6"
	blank lines before: 0
	blank lines after: 1

scene:
	left margin: 1.5"
	right margin:
		7.5" from left,
		1" from right
	width: 6"
	blank lines before: 2
	blank lines after: 1

action:
	left margin: 1.5"
	right margin:
		7.5" from left,
		1" from right
	width: 6"
	blank lines before: 1
	blank lines after: 1

character:
	left margin: 4.2"
	right margin:
		7.5" from left,
		1" from right
	width: 3.3"
	blank lines before:
		elsewhere: 1
	blank lines after: 0

dialogue:
	left margin: 2.9"
	right margin:
		6.2" from left,
		2.3" from right
	width: 3.3"
	blank lines before: 0
	blank lines after:
		if parenthetical is next: 0
		all others: 1

parenthetical:
	left margin: 3.6"
	right margin:
		5.6" from left,
		2.9" from right
	width: 2"
	blank lines before: 0
	blank lines after:
		if dialogue is next: 0
		all others: 1

transition:
	left margin: 6"
	right margin:
		7.5" from left,
		1" from right
	width: 1.5"
	blank lines before: 1
	blank lines after: 2

subheader:
	left margin: 1.5"
	right margin:
		7.5" from left,
		1" from right
	width: 6"
	blank lines before: 1
	blank lines after: 1

'''

