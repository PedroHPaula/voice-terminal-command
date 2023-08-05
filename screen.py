from curses import initscr, endwin, \
					curs_set, flushinp,\
					noecho, cbreak, \
					echo, nocbreak, \
					A_BLINK, A_BOLD
from signal import signal, SIGWINCH

# Class that handles the display of the main script's terminal screen
class ScriptScreen:
	
	name = "MainScreen"

	messages = {
		'input'       : '>>> Awaiting Voice Input <<<',
		'validate'    : 'Validating Voice Input...',
		'invalid'     : "The sentence couldn't be validated",
		'short'       : 'The input was too short',
		'please'      : 'Please, try speaking again',
		'control_on'  : 'CONTROL ON',
		'control_off' : 'control off',
		'shift_on'    : 'SHIFT   ON',
		'shift_off'   : 'shift   off',
	}

	def __init__(self):

		self.input_flag = 1
		self.invalid_flag = 0
		self.short_flag = 0

		self.last_command = ''
		self.control_flag = 0
		self.shift_flag = 0

		# Set the handler for signal SIGWINCH to the method resize_handler.
		# Everytime the winodw is resized, resize_handler will be called to refresh it.
		signal(SIGWINCH, self.resize_handler)

		# Start curses mode and set display properties.
		self.stdscr = initscr()
		self.set_general_props()
		self.stdscr.clear()
		rows, cols = self.stdscr.getmaxyx()
		self.print_input(rows, cols)
		self.stdscr.refresh()

	def set_general_props(self):
		noecho()
		cbreak()
		curs_set(0)
		self.stdscr.keypad(1)

	def clear_general_props(self):
		echo()
		nocbreak()
		curs_set(1)
		self.stdscr.keypad(0)

	def print_input(self, rows, cols):
		y = int(rows/2)
		x = int((cols-len(self.messages['input']))/2)
		if y >= 0 and y <= rows and x >= 0 and x <= (cols-len(self.messages['input'])): 
			self.stdscr.attron(A_BOLD)
			self.stdscr.attron(A_BLINK)
			self.stdscr.addstr(y, x, self.messages['input'])
			self.stdscr.attroff(A_BOLD)
			self.stdscr.attroff(A_BLINK)

	def print_parse(self, rows, cols):
		y = int(rows/2)
		x = int((cols-len(self.messages['validate']))/2)
		if y >= 0 and y <= rows and x >= 0 and x <= (cols-len(self.messages['validate'])): 
			self.stdscr.attron(A_BOLD)
			self.stdscr.addstr(y, x, self.messages['validate'])
			self.stdscr.attroff(A_BOLD)

	def print_invalid(self, rows, cols):
		y1 = int(rows/2)+2
		x1 = int((cols-len(self.messages['invalid']))/2)
		if y1 >= 0 and y1 <= rows and x1 >= 0 and x1 <= (cols-len(self.messages['invalid'])):
			self.stdscr.attron(A_BOLD)
			self.stdscr.addstr(y1, x1, self.messages['invalid'])
			y2 = y1+1
			x2 = int((cols-len(self.messages['please']))/2)
			if y2 <= (rows-2) and x2 >= 0 and x2 <= (cols-len(self.messages['please'])):
				self.stdscr.addstr(y2, x2, self.messages['please'])
			self.stdscr.attroff(A_BOLD)

	def print_short(self, rows, cols):
		y1 = int(rows/2)+2
		x1 = int((cols-len(self.messages['short']))/2)
		if y1 >= 0 and y1 <= rows and x1 >= 0 and x1 <= (cols-len(self.messages['short'])):
			self.stdscr.attron(A_BOLD)
			self.stdscr.addstr(y1, x1, self.messages['short'])
			y2 = y1+1
			x2 = int((cols-len(self.messages['please']))/2)
			if y2 <= (rows-2) and x2 >= 0 and x2 <= (cols-len(self.messages['please'])):
				self.stdscr.addstr(y2, x2, self.messages['please'])
			self.stdscr.attroff(A_BOLD)

	def print_command(self, rows, cols):
		y = int(rows/2)+2
		x = int((cols-len(self.last_command))/2)
		if y >= 0 and y <= (rows-2) and x >= 0 and x <= (cols-len(self.last_command)): 
			self.stdscr.attron(A_BOLD)
			self.stdscr.addstr(y, x, self.last_command)
			self.stdscr.attroff(A_BOLD)

	def print_key_state(self, rows, cols):
			y1 = int(rows/2)-3
			x1 = 1
			if y1 >= 0: 
				if self.control_flag:
					self.stdscr.attron(A_BOLD)
					self.stdscr.addstr(y1, x1, self.messages['control_on'])
					self.stdscr.attroff(A_BOLD)
				else:
					self.stdscr.addstr(y1, x1, self.messages['control_off'])
			y2 = y1 + 1
			x2 = 1
			if y2 >= 0:
				if self.shift_flag:
					self.stdscr.attron(A_BOLD)
					self.stdscr.addstr(y2, x2, self.messages['shift_on'])
					self.stdscr.attroff(A_BOLD)
				else:
					self.stdscr.addstr(y2, x2, self.messages['shift_off'])
				
	def update(self):
		try:
			self.stdscr.clear()
			rows, cols = self.stdscr.getmaxyx()
			if self.input_flag and self.short_flag:
				self.print_input(rows, cols)
				self.print_short(rows,cols)
			elif self.input_flag and not self.invalid_flag:
				self.print_input(rows, cols)
				self.print_command(rows, cols)
			elif self.input_flag and self.invalid_flag:
				self.print_input(rows, cols)
				self.print_invalid(rows, cols)
			elif not self.input_flag:
				self.print_parse(rows, cols)
			self.print_key_state(rows, cols)
			self.stdscr.refresh()
		# Curses raises an error when we try to print something out of the the screen's coordinates
		# So we want to just ignore it and keep the script runnng until the window is resized.
		except:
			pass

	def resize_handler(self, signum, frame):
		endwin()
		self.stdscr.refresh()
		self.update()

	def exit(self):
		# flushinp is necessary to clear any characters 
		# that the user may have inputted during curses mode.
		flushinp()
		self.clear_general_props()
		self.stdscr.clear()
		endwin()