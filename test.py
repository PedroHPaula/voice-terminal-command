#! /usr/bin/python3 -u

import os
from pynput.keyboard import Key, Controller
import shlex
import subprocess
from shutil import which
import time

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

ARROW_KEYS = {
    'DOWN'  : Key.down,
	'LEFT'  : Key.left,
    'RIGHT' : Key.right,
	'UP'    : Key.up,
	'UPPER' : Key.up,
}

alt_actions = {
		**DIGITS_STRINGS,
		**ARROW_KEYS
}

print(alt_actions)