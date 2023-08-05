#! /usr/bin/python3

from pynput.keyboard import Key

ARROW_KEYS = {
	'DOWN'  : Key.down,
	'LEFT'  : Key.left,
    'RIGHT' : Key.right,
	'UP'    : Key.up,
	'UPPER' : Key.up,
}

ALPHABET_KEYS = {
	'A'     : 'a',
	'C'     : 'c',
	'E'     : 'e',
	'K'     : 'k',
	'L'     : 'l',
    'O'     : 'o',
	'V'     : 'v',
    'X'     : 'x',
	'Z'     : 'z',
}

ALPHANUM_KEYS = {
	'ENTER'      : Key.enter,
	'SPACE'      : Key.space,
	'TAB'        : Key.tab,
	'TABULAR'    : Key.tab,
	'TABULATE'   : Key.tab,
	'CAPS'       : Key.caps_lock,
	'LOCK'       : Key.caps_lock,
	'CAPS LOCK'  : Key.caps_lock,
	'SHIFT'      : Key.shift,
	**ALPHABET_KEYS
}

CONTROL_KEYS = {
	'ESCAPE'       : Key.esc,
	'PRINT'        : Key.print_screen,
	'PRINT SCREEN' : Key.print_screen,
	'SCROLL'       : Key.scroll_lock,
	'SCROLL LOCK'  : Key.scroll_lock,
	'PAUSE'        : Key.pause,
	'PAUSE BREAK'  : Key.pause,
	'CONTROL'      : Key.ctrl,
	'WINDOWS'      : Key.cmd,
	'SUPER'        : Key.cmd,
	'ALT'          : Key.alt,
	'MENU'         : Key.menu,
}

CONTROL_KEY_ACTIONS = {
	'CLEAR'  : 'l',
	'CLIP'   : 'x',
	'COPY'   : 'c',
	'CUT'    : 'x',
	'PASTE'  : 'v',
	'SAVE'   : 's',
	'SEARCH' : 'f',
	'SELECT' : 'a',
	'UNDO'   : 'z',
}

DIGITS_STRINGS = {
	'ZERO'  : '0',
	'ONE'   : '1',
	'TWO'   : '2',
    'THREE' : '3',
    'FOUR'  : '4',
    'FIVE'  : '5',
    'SIX'   : '6',
    'SEVEN' : '7',
    'EIGHT' : '8',
    'NINE'  : '9',
}

DIGITS_INTS = {
	'ZERO'  : 0,
	'ONE'   : 1,
	'TWO'   : 2,
    'THREE' : 3,
    'FOUR'  : 4,
    'FIVE'  : 5,
    'SIX'   : 6,
    'SEVEN' : 7,
    'EIGHT' : 8,
    'NINE'  : 9,
}

#FUNCTION_KEYS = {}

NAVIGATION_KEYS = {
	'INSERT'     : Key.insert,
	'DELETE'     : Key.delete,
	'HOME'       : Key.home,
	'END'        : Key.end,
	'PAGE UP'    : Key.page_up,
	'PAGE UPPER' : Key.page_up,
	'PAGE DOWN'  : Key.page_down,
    **ARROW_KEYS
}

TERMINAL_COMMANDS = {
	'ARGUMENT'     : 'xargs',
	'COPY'         : 'cp',
	'CD'           : 'cd',
	'CLEAR'        : 'clear',
	'DIRECTORY'    : 'mkdir',
	'DIRECTORY(4)' : 'mkdir',
	'ECHO'         : 'echo',
	'EXIT'         : 'exit',
	'FIND'         : 'find',
	'GIT'          : 'git',
	'GLOBAL'       : 'grep',
	'LESS'         : 'less',
	'LIST'         : 'ls',
	'LOCATE'       : 'plocate',
	'MAN'          : 'man',
	'MOVE'         : 'mv',
	'NANO'         : 'nano',
	'NEW'          : 'gnome-terminal',
	'PIPE'         : '|',
	'PIPELINE'     : '|',
	'REMOVE'       : 'rm',
	'SILENCE'      : 'silence',
	'STREAM'       : 'sed',
	'SWITCH'       : 'sudo',
	'TAR'          : 'tar',
	'ZIP'          : 'gzip',
}