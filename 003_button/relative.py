import os
from tkinter import *

class RelativeImagePath:
	def get_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		relative_file_name = PhotoImage(file = path)

		return relative_file_name
