from tkinter import *
from tkinter import font
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Step Through System Font List")
		self.width = 450
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		fonty_label = FontyLabel(self)
		# layout
		fonty_label.grid(column = 1, row = 0)

class FontyLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.font_family_list = list(font.families())
		self.font_index = 0
		self.font_style = font.Font(family = self.font_family_list[self.font_index])
		self.text = "Configuration with Style"
		self.width = len(self.text) # width is in characters
		# configure
		self.config(anchor = "c", text = self.text, width = self.width)
		self.config(text = self.font_family_list[self.font_index], font = self.font_style)
		self.list_fonts()

	def list_fonts(self):
		for font_family in self.font_family_list:
			print(f"font_family: {font_family}")
			self.config(font = font.Font(family = font_family), text = font_family)


if __name__ == "__main__":
	main()

'''
font_family: System
font_family: Terminal
font_family: Fixedsys
font_family: Modern
font_family: Roman
font_family: Script
font_family: Courier
font_family: MS Serif
font_family: MS Sans Serif
font_family: Small Fonts
font_family: Adobe Arabic
font_family: Adobe Hebrew
font_family: Adobe Ming Std L
font_family: @Adobe Ming Std L
font_family: Adobe Myungjo Std M
font_family: @Adobe Myungjo Std M
font_family: Adobe Song Std L
font_family: @Adobe Song Std L
font_family: Kozuka Gothic Pro B
font_family: @Kozuka Gothic Pro B
font_family: Kozuka Gothic Pro EL
font_family: @Kozuka Gothic Pro EL
font_family: Kozuka Gothic Pro H
font_family: @Kozuka Gothic Pro H
font_family: Kozuka Gothic Pro L
font_family: @Kozuka Gothic Pro L
font_family: Kozuka Gothic Pro M
font_family: @Kozuka Gothic Pro M
font_family: Kozuka Gothic Pro R
font_family: @Kozuka Gothic Pro R
font_family: Kozuka Mincho Pro B
font_family: @Kozuka Mincho Pro B
font_family: Kozuka Mincho Pro EL
font_family: @Kozuka Mincho Pro EL
font_family: Kozuka Mincho Pro H
font_family: @Kozuka Mincho Pro H
font_family: Kozuka Mincho Pro L
font_family: @Kozuka Mincho Pro L
font_family: Kozuka Mincho Pro M
font_family: @Kozuka Mincho Pro M
font_family: Kozuka Mincho Pro R
font_family: @Kozuka Mincho Pro R
font_family: Letter Gothic Std
font_family: Minion Pro
font_family: Myriad Pro
font_family: Myriad Pro Cond
font_family: Myriad Pro Light
font_family: Adobe Caslon Pro Bold
font_family: Adobe Caslon Pro
font_family: Adobe Fangsong Std R
font_family: @Adobe Fangsong Std R
font_family: Adobe Fan Heiti Std B
font_family: @Adobe Fan Heiti Std B
font_family: Adobe Gothic Std B
font_family: @Adobe Gothic Std B
font_family: Adobe Heiti Std R
font_family: @Adobe Heiti Std R
font_family: Adobe Kaiti Std R
font_family: @Adobe Kaiti Std R
font_family: Adobe Garamond Pro Bold
font_family: Adobe Garamond Pro
font_family: Birch Std
font_family: Blackoak Std
font_family: Brush Script Std
font_family: Chaparral Pro
font_family: Charlemagne Std
font_family: Cooper Std Black
font_family: Giddyup Std
font_family: Hobo Std
font_family: Kozuka Gothic Pr6N B
font_family: @Kozuka Gothic Pr6N B
font_family: Kozuka Gothic Pr6N EL
font_family: @Kozuka Gothic Pr6N EL
font_family: Kozuka Gothic Pr6N H
font_family: @Kozuka Gothic Pr6N H
font_family: Kozuka Gothic Pr6N L
font_family: @Kozuka Gothic Pr6N L
font_family: Kozuka Gothic Pr6N M
font_family: @Kozuka Gothic Pr6N M
font_family: Kozuka Gothic Pr6N R
font_family: @Kozuka Gothic Pr6N R
font_family: Kozuka Mincho Pr6N B
font_family: @Kozuka Mincho Pr6N B
font_family: Kozuka Mincho Pr6N EL
font_family: @Kozuka Mincho Pr6N EL
font_family: Kozuka Mincho Pr6N H
font_family: @Kozuka Mincho Pr6N H
font_family: Kozuka Mincho Pr6N L
font_family: @Kozuka Mincho Pr6N L
font_family: Kozuka Mincho Pr6N M
font_family: @Kozuka Mincho Pr6N M
font_family: Kozuka Mincho Pr6N R
font_family: @Kozuka Mincho Pr6N R
font_family: Lithos Pro Regular
font_family: Mesquite Std
font_family: Minion Pro Cond
font_family: Minion Pro Med
font_family: Minion Pro SmBd
font_family: Nueva Std Cond
font_family: OCR A Std
font_family: Orator Std
font_family: Poplar Std
font_family: Prestige Elite Std
font_family: Rosewood Std Regular
font_family: Stencil Std
font_family: Tekton Pro
font_family: Tekton Pro Cond
font_family: Tekton Pro Ext
font_family: Trajan Pro
font_family: Nachlieli CLM
font_family: Frank Ruhl Hofshi
font_family: Miriam Libre
font_family: Marlett
font_family: Arial
font_family: Arabic Transparent
font_family: Arial Baltic
font_family: Arial CE
font_family: Arial CYR
font_family: Arial Greek
font_family: Arial TUR
font_family: Arial Black
font_family: Bahnschrift Light
font_family: Bahnschrift SemiLight
font_family: Bahnschrift
font_family: Bahnschrift SemiBold
font_family: Bahnschrift Light SemiCondensed
font_family: Bahnschrift SemiLight SemiConde
font_family: Bahnschrift SemiCondensed
font_family: Bahnschrift SemiBold SemiConden
font_family: Bahnschrift Light Condensed
font_family: Bahnschrift SemiLight Condensed
font_family: Bahnschrift Condensed
font_family: Bahnschrift SemiBold Condensed
font_family: Calibri
font_family: Calibri Light
font_family: Cambria
font_family: Cambria Math
font_family: Candara
font_family: Candara Light
font_family: Comic Sans MS
font_family: Consolas
font_family: Constantia
font_family: Corbel
font_family: Corbel Light
font_family: Courier New
font_family: Courier New Baltic
font_family: Courier New CE
font_family: Courier New CYR
font_family: Courier New Greek
font_family: Courier New TUR
font_family: Ebrima
font_family: Franklin Gothic Medium
font_family: Gabriola
font_family: Gadugi
font_family: Georgia
font_family: Impact
font_family: Ink Free
font_family: Javanese Text
font_family: Leelawadee UI
font_family: Leelawadee UI Semilight
font_family: Lucida Console
font_family: Lucida Sans Unicode
font_family: Malgun Gothic
font_family: @Malgun Gothic
font_family: Malgun Gothic Semilight
font_family: @Malgun Gothic Semilight
font_family: Microsoft Himalaya
font_family: Microsoft JhengHei
font_family: @Microsoft JhengHei
font_family: Microsoft JhengHei UI
font_family: @Microsoft JhengHei UI
font_family: Microsoft JhengHei Light
font_family: @Microsoft JhengHei Light
font_family: Microsoft JhengHei UI Light
font_family: @Microsoft JhengHei UI Light
font_family: Microsoft New Tai Lue
font_family: Microsoft PhagsPa
font_family: Microsoft Sans Serif
font_family: Microsoft Tai Le
font_family: Microsoft YaHei
font_family: @Microsoft YaHei
font_family: Microsoft YaHei UI
font_family: @Microsoft YaHei UI
font_family: Microsoft YaHei Light
font_family: @Microsoft YaHei Light
font_family: Microsoft YaHei UI Light
font_family: @Microsoft YaHei UI Light
font_family: Microsoft Yi Baiti
font_family: MingLiU-ExtB
font_family: @MingLiU-ExtB
font_family: PMingLiU-ExtB
font_family: @PMingLiU-ExtB
font_family: MingLiU_HKSCS-ExtB
font_family: @MingLiU_HKSCS-ExtB
font_family: Mongolian Baiti
font_family: MS Gothic
font_family: @MS Gothic
font_family: MS UI Gothic
font_family: @MS UI Gothic
font_family: MS PGothic
font_family: @MS PGothic
font_family: MV Boli
font_family: Myanmar Text
font_family: Nirmala UI
font_family: Nirmala UI Semilight
font_family: Palatino Linotype
font_family: Segoe MDL2 Assets
font_family: Segoe Print
font_family: Segoe Script
font_family: Segoe UI
font_family: Segoe UI Black
font_family: Segoe UI Emoji
font_family: Segoe UI Historic
font_family: Segoe UI Light
font_family: Segoe UI Semibold
font_family: Segoe UI Semilight
font_family: Segoe UI Symbol
font_family: SimSun
font_family: @SimSun
font_family: NSimSun
font_family: @NSimSun
font_family: SimSun-ExtB
font_family: @SimSun-ExtB
font_family: Sitka Small
font_family: Sitka Text
font_family: Sitka Subheading
font_family: Sitka Heading
font_family: Sitka Display
font_family: Sitka Banner
font_family: Sylfaen
font_family: Symbol
font_family: Tahoma
font_family: Times New Roman
font_family: Times New Roman Baltic
font_family: Times New Roman CE
font_family: Times New Roman CYR
font_family: Times New Roman Greek
font_family: Times New Roman TUR
font_family: Trebuchet MS
font_family: Verdana
font_family: Webdings
font_family: Wingdings
font_family: Yu Gothic
font_family: @Yu Gothic
font_family: Yu Gothic UI
font_family: @Yu Gothic UI
font_family: Yu Gothic UI Semibold
font_family: @Yu Gothic UI Semibold
font_family: Yu Gothic Light
font_family: @Yu Gothic Light
font_family: Yu Gothic UI Light
font_family: @Yu Gothic UI Light
font_family: Yu Gothic Medium
font_family: @Yu Gothic Medium
font_family: Yu Gothic UI Semilight
font_family: @Yu Gothic UI Semilight
font_family: HoloLens MDL2 Assets
font_family: Myriad Web Pro
font_family: ZWAdobeF
font_family: Agency FB
font_family: Arial Narrow
font_family: Arial Rounded MT Bold
font_family: Blackadder ITC
font_family: Bodoni MT
font_family: Bodoni MT Black
font_family: Bodoni MT Condensed
font_family: Book Antiqua
font_family: Bookman Old Style
font_family: Bradley Hand ITC
font_family: Calisto MT
font_family: Castellar
font_family: Century Gothic
font_family: Century Schoolbook
font_family: Copperplate Gothic Bold
font_family: Copperplate Gothic Light
font_family: Curlz MT
font_family: Edwardian Script ITC
font_family: Elephant
font_family: Engravers MT
font_family: Eras Bold ITC
font_family: Eras Demi ITC
font_family: Eras Light ITC
font_family: Eras Medium ITC
font_family: Felix Titling
font_family: Forte
font_family: Franklin Gothic Book
font_family: Franklin Gothic Demi
font_family: Franklin Gothic Demi Cond
font_family: Franklin Gothic Heavy
font_family: Franklin Gothic Medium Cond
font_family: French Script MT
font_family: Garamond
font_family: Gigi
font_family: Gill Sans MT Ext Condensed Bold
font_family: Gill Sans MT
font_family: Gill Sans MT Condensed
font_family: Gill Sans Ultra Bold
font_family: Gill Sans Ultra Bold Condensed
font_family: Gloucester MT Extra Condensed
font_family: Goudy Old Style
font_family: Goudy Stout
font_family: Haettenschweiler
font_family: Imprint MT Shadow
font_family: Lucida Sans
font_family: Lucida Sans Typewriter
font_family: Maiandra GD
font_family: Monotype Corsiva
font_family: OCR A Extended
font_family: Palace Script MT
font_family: Papyrus
font_family: Perpetua
font_family: Perpetua Titling MT
font_family: Pristina
font_family: Rage Italic
font_family: Rockwell
font_family: Rockwell Condensed
font_family: Rockwell Extra Bold
font_family: Script MT Bold
font_family: Tw Cen MT
font_family: Tw Cen MT Condensed
font_family: Wingdings 2
font_family: Wingdings 3
font_family: Bookshelf Symbol 7
font_family: MS Reference Sans Serif
font_family: MS Reference Specialty
font_family: Tw Cen MT Condensed Extra Bold
font_family: ModeNine
font_family: C64 Pro Mono
font_family: Linux Biolinum G
font_family: Amiri
font_family: Carlito
font_family: David CLM
font_family: Liberation Sans Narrow
font_family: OpenSymbol
font_family: Reem Kufi
font_family: Noto Kufi Arabic
font_family: Alef
font_family: David Libre
font_family: EmojiOne Color
font_family: Source Code Pro Black
font_family: Liberation Mono
font_family: Source Serif Pro Black
font_family: Gentium Basic
font_family: Source Sans Pro Black
font_family: Scheherazade
font_family: KacstBook
font_family: DejaVu Math TeX Gyre
font_family: Caladea
font_family: Amiri Quran
font_family: Frank Ruehl CLM
font_family: Miriam CLM
font_family: Miriam Mono CLM
font_family: DejaVu Sans
font_family: DejaVu Sans Light
font_family: DejaVu Sans Condensed
font_family: DejaVu Sans Mono
font_family: DejaVu Serif
font_family: DejaVu Serif Condensed
font_family: Gentium Book Basic
font_family: KacstOffice
font_family: Liberation Sans
font_family: Liberation Serif
font_family: Linux Libertine Display G
font_family: Linux Libertine G
font_family: Rubik
font_family: Noto Mono
font_family: Noto Naskh Arabic
font_family: Noto Naskh Arabic UI
font_family: Noto Sans
font_family: Noto Sans Cond
font_family: Noto Sans Light
font_family: Noto Sans Arabic
font_family: Noto Sans Arabic UI
font_family: Noto Sans Armenian
font_family: Noto Sans Georgian
font_family: Noto Sans Hebrew
font_family: Noto Sans Lao
font_family: Noto Sans Lisu
font_family: Noto Serif
font_family: Noto Serif Cond
font_family: Noto Serif Light
font_family: Noto Serif Armenian
font_family: Noto Serif Georgian
font_family: Noto Serif Hebrew
font_family: Noto Serif Lao
font_family: Source Code Pro
font_family: Source Code Pro ExtraLight
font_family: Source Code Pro Light
font_family: Source Code Pro Medium
font_family: Source Code Pro Semibold
font_family: Source Sans Pro
font_family: Source Sans Pro ExtraLight
font_family: Source Sans Pro Light
font_family: Source Sans Pro Semibold
font_family: Source Serif Pro
font_family: Source Serif Pro ExtraLight
font_family: Source Serif Pro Light
font_family: Source Serif Pro Semibold
font_family: TtsNote
font_family: Trek
'''