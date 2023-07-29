#! /usr/bin/python3 -u
# (Note: The -u disables buffering, as else we don't get Julius's output.)
#
# Command and Control Application for Julius
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Julius OUTPUT FORMAT:	

		#pass1_best: <s> COMMAND
		#pass1_best_wordseq: 0 2
		#pass1_best_phonemeseq: sil | k ah m ae n d
		#pass1_best_score: -3597.272217
		### Recognition: 2nd pass (RL heuristic best-first)
        #STAT: 00 _default: 19 generated, 19 pushed, 5 nodes popped in 126
        #sentence1: <s> CONTROL V </s>
        #wseq1: 0 3 6 1
        #phseq1: sil | k ah n t r ow l | v iy | sil
        #cmscore1: 1.000 1.000 0.965 1.000
        #score1: -10582.712891

import shlex
import subprocess
import sys
from time import sleep
from pynput.keyboard import Key, Controller
from constants import ARROW_KEYS, ALPHABET_KEYS, ALPHANUM_KEYS, \
					  CONTROL_KEYS, CONTROL_KEY_ACTIONS, DIGITS_STRINGS, \
					  DIGITS_INTS, NAVIGATION_KEYS, TERMINAL_COMMANDS

# Function that returns info about the current active window
def active_window():

	# Command to get the id of the current active window
	xprop_command="/usr/bin/xprop -root _NET_ACTIVE_WINDOW"
	args = shlex.split(xprop_command)
	process = subprocess.run(args, capture_output=True, encoding="UTF-8")
	window_id = process.stdout[40:49]

	# Use the id to get the string that contains the name of the current active window
	xprop_command="/usr/bin/xprop -id " + window_id + " WM_NAME"
	args = shlex.split(xprop_command)
	active_window_str = subprocess.run(args, capture_output=True, encoding="UTF-8")
	
	return [window_id, active_window_str.stdout] 

# Class for general commands that are not associated with the Terminal
class General:

	name = "General"

	alt_actions = {
		**ARROW_KEYS,
		**DIGITS_STRINGS
	}

	ctrl_actions = {
		**ARROW_KEYS,
		**CONTROL_KEY_ACTIONS
	}


	hold_actions = {
        'CONTROL' : Key.ctrl,
        'SHIFT'   : Key.shift,
    }

	press_actions = {
		**ALPHANUM_KEYS,
		**CONTROL_KEYS,
		**NAVIGATION_KEYS
	}

	shift_actions = {
		**DIGITS_STRINGS
	}
    
	super_actions = {
		**NAVIGATION_KEYS
	}

	action_types = {
		'alt_actions'   : alt_actions,
		'ctrl_actions'  : ctrl_actions,
		'hold_actions'  : hold_actions,
		'press_actions' : press_actions,
		'shift_actions' : shift_actions,
		'super_actions' : super_actions,
	}

	# Method that parses the strings equivalent to the spoken commands
	def parse_general_commands(self, action_str, action_type):
		if action_str in self.action_types[action_type]:
			return self.action_types[action_type][action_str]
	
# Class for Terminal-only commands
class Terminal:

	name = "Terminal"
    
	commands = {
		**TERMINAL_COMMANDS
	}
	
	# Method that parses the strings equivalent to the spoken commands
	def parse_terminal_commands(self, command):
		if command in self.commands:
			return self.commands[command]

	# Method that opens a new terminal window	
	def new_terminal(self):
		new_terminal_command="/usr/bin/gnome-terminal"
		args = shlex.split(new_terminal_command)
		output = subprocess.run(args, capture_output=True, encoding="UTF-8")
		return output
	
	# Method that exits the current active terminal window	
	def exit_terminal(self,keyboard):
		with keyboard.pressed(Key.ctrl):
			keyboard.press('d')
			keyboard.release('d')
# Main class
class CommandAndControl:

	def __init__(self, file_object, script_id):
	
		self.general = General()
		
		self.keyboard = Controller()
	
		self.terminal = Terminal()
		
		# Flag to determine if setence validation is necessary
		check_cmscore = 0
		
		print('>>> Awaiting Input <<<',end='\n\n')

		while 1:
			# Store each line of Julius output as a string
			julius_line = file_object.readline()
			
			# Await until Julius output a valid string
			if not julius_line:
				break
			if julius_line:
				# If no validation was made, store the current recognized sentence
				# And set the flag to validate the sentence
				if check_cmscore == 0:
					if julius_line.startswith('sentence1: <s>') and julius_line.endswith(' </s>\n'):
					
						check_cmscore = 1
						
						sentence = julius_line.replace('sentence1: <s> ','').replace(' </s>\n','')
					# Await for the next user's input in case the sentence has been already validated
					elif julius_line.startswith('score1: '):
						print('>>> Awaiting Input <<<',end='\n\n')
				# Validate the stored sentence and set the validation flag to zero
				elif check_cmscore == 1:
					if julius_line.startswith('cmscore1: ') and julius_line.endswith('\n'):
			
						check_cmscore = 0
						
						cmscore = julius_line.replace('cmscore1: ','').replace('\n','').split(' ')
						
						print('\t\t\t',sentence,' - ',min(cmscore),end='\n\n')
						
						# Check the current active window
						current_window_info = active_window()
						win_id = current_window_info[0]
						win_name = current_window_info[1]

						# Pass score that determines if the spoken sentence is valid
						if float(min(cmscore)) >= 0.700:
							# Alt Key valid actions
							if sentence.startswith('ALT') and win_id != script_id:

								substr = sentence.replace('ALT ','')
								alt_action = self.general.parse_general_commands(substr,'alt_actions')
								if alt_action:
									with self.keyboard.pressed(Key.alt):
											self.keyboard.press(alt_action)
											self.keyboard.release(alt_action)

								else:
									print('\t','The Alt action ', substr,' is not supported',end='\n\n')
							# Terminal valid commands (only works if there is a current active Terminal window)
							elif sentence.startswith('COMMAND') and win_id != script_id and \
								'"Terminal"' in win_name:
								
								substr = sentence.replace('COMMAND ','')
								command = self.terminal.parse_terminal_commands(substr)
								if command:								
									self.keyboard.type(command)

								else:
									print('\t','The Command action ', substr,' is not supported',end='\n\n')							
							# Control Key valid actions
							elif sentence.startswith('CONTROL') and win_id != script_id:
								
								substr = sentence.replace('CONTROL ','')
								ctrl_action = self.general.parse_general_commands(substr,'ctrl_actions')
								if ctrl_action:
									with self.keyboard.pressed(Key.ctrl):
											self.keyboard.press(ctrl_action)
											self.keyboard.release(ctrl_action)

								else:
									print('\t','The Control action ', substr,' is not supported',end='\n\n')
							# Hold valid actions
							elif sentence.startswith('HOLD') and win_id != script_id:
								
								substr = sentence.replace('HOLD ','')
								hold_action = self.general.parse_general_commands(substr,'hold_actions')
								if hold_action:
									self.keyboard.press(hold_action)
									print('\t\t','The ', substr, ' key is Pressed',end='\n\n')
									sleep(5.0)
									self.keyboard.release(hold_action)
									print('\t\t','The ', substr, ' key is Released',end='\n\n')																			

								else:
									print('\t','The Hold action ', substr,' is not supported',end='\n\n')
							# Press valid actions
							elif sentence.startswith('PRESS') and win_id != script_id:
								
								sentence_words = sentence.rsplit()

								# Check if the sentence ends with a non-zero numeral
								if sentence_words[-1] != 'ZERO' and sentence_words[-1] in DIGITS_STRINGS:
									n = DIGITS_INTS[sentence_words[-1]]
									sentence_words.pop()
								else:
									n = 1
								
								# Pass only the action words of the sentence
								sentence_words.pop(0)
								press_action = self.general.parse_general_commands(' '.join(sentence_words),'press_actions')

								if press_action:					
									for i in range(n):
										self.keyboard.tap(press_action)
								else:
									print('\t','The Press action ', ' '.join(sentence_words),' is not supported',end='\n\n')

							elif sentence.startswith('SHIFT') and win_id != script_id:
								
								substr = sentence.replace('SHIFT ','')
								shift_action = self.general.parse_general_commands(substr,'shift_actions')
								if shift_action:
									with self.keyboard.pressed(Key.shift):
										self.keyboard.press(shift_action)
										self.keyboard.release(shift_action)
										
								else:
									print('\t','The Super action ', substr,' is not supported',end='\n\n')
							# Super (i.e. W!n or command key) valid actions
							elif sentence.startswith('SUPER') or sentence.startswith('WINDOWS'):
								
								substr = sentence.replace('SUPER ','').replace('WINDOWS ','')
								super_action = self.general.parse_general_commands(substr,'super_actions')
								if super_action:
									with self.keyboard.pressed(Key.cmd):
										self.keyboard.press(super_action)
										self.keyboard.release(super_action)
										
								else:
									print('\t','The Super action ', substr,' is not supported',end='\n\n')
							# Terminal valid commands (only works if there is a current active Terminal window)
							elif sentence.startswith('TERMINAL') and '"Terminal"' in win_name:
								
								substr = sentence.replace('TERMINAL ','')
								command = self.terminal.parse_terminal_commands(substr)
								if command == 'gnome-terminal':
									self.terminal.new_terminal()									
								elif command == 'exit' and win_id != script_id:
									self.terminal.exit_terminal(self.keyboard)
								elif command == 'silence':
									sys.exit(2)
								elif command and win_id != script_id:								
									self.keyboard.type(command)

								else:
									print( '\t','The Terminal action ', substr,' is not supported',end='\n\n')	
						# Print a message if the sentence could not be validated
						else:
							print('\t','Sorry, the sentence could not be validated.\n','\t','Please try speaking again',end='\n\n')
					

if __name__ == '__main__':
	try:
		
		# The id of the script's window is necessary to validate
		# If some commands can be executed
		script_window_id = active_window()[0]

		# Start Julius with the specified configuration file
		# And pipe its output to the main class. 
		# Standard error is directed to os.devnull.
		julius_command="./julius -C terminal.jconf"
		args = shlex.split(julius_command)
		julius_output = subprocess.Popen(
			args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="UTF-8")

		CommandAndControl(julius_output.stdout, script_window_id)

	except KeyboardInterrupt:
		sys.exit(1)
