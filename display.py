import lcddriver

class display:

	def __init__(self, chars, lines):
		self.chars = chars
		self.lines = lines
		self.display = lcddriver.lcd()

	def print_right(self, string, line=1):
		if(isinstance(string, list)):
			for s in string:
				space = ''
				offset = self.chars - len(s)
				if(offset < 0):
					offset = 0	
				for space in range(0, offset):
					space += ' '
				display.lcd_display_string(space + s, line++)
		else:
			space = ''
			offset = self.chars - len(string)
			if(offset < 0):
				offset = 0	
			for space in range(0, offset):
				space += ' '
			display.lcd_display_string(space + string, line)

	def print_center(self, string, line=1):
		if(isinstance(string, list)):
			for s in string:
				space = ''
				offset = int(self.chars / 2) - int(len(s) / 2)
				for space in range(0, offset):
					space += ' '
				display.lcd_display_string(space + s, line++)
		else:
			space = ''
			offset = int(self.chars / 2) - int(len(string) / 2)
			for space in range(0, offset):
				space += ' '
			display.lcd_display_string(space + string, line)


	def print(self, string, line=1):
		if(isinstance(string, list)):
			for s in string:
				display.lcd_display_string(s, line++)
		else:
			display.lcd_display_string(string, line)




