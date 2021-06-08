from tkinter import *
from tkinter import ttk
from tkinter import font

class AppStyle(ttk.Style):
	def __init__(self):
		super().__init__()
		# class attributes
		self.themes = self.theme_names()
		self.theme_use('default')
		# configure derivative styles
		self.show_all()

	def show_all(self):
		print("TButton.border:")
		print(f"{self.element_options('TButton.border')}")
		print("TButton.label:")
		print(f"{self.element_options('TButton.label')}")
		print("TButton.focus:")
		print(f"{self.element_options('TButton.focus')}")
		print("TButton.spacing:")
		print(f"{self.element_options('TButton.spacing')}")

style = AppStyle()

print(f"Themes: {style.themes}")

for theme in style.themes:
	print(f"{theme}")
	
