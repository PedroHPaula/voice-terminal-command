# Overview
A simple Python script to use Linux Terminal commands and other commands, 
such as keyboard shortcuts. It works by getting a text output
that represents user's input voice from the microphone of his device
and inserting text or performing the desired action via voice command. The transcription
from voice to text in real time is performed by the [Julius](https://github.com/julius-speech/julius) speech
engine.
# How to use
To run the script you will need (besides the dependencies listed below) to open a Linux Terminal and execution permission.
After that the open terminal window will keep listening to the inputs from the microphone and trying to validate the spoken
sentences into valid actions. The specific sentence <b>"TERMINAL SILENCE"</b> is reserved to be used when you want to exit the script, it only works when a terminal window is active. You could also interrupt it using <b>Ctrl+C</b> in the terminal where it was called. Furthermore, the <b>"TERMINAL NEW"</b> voice command opens a new terminal window when the script's window is active. 


The following table displays the currently
supported terminal commands. The voice command can be either preceded by the <b>"TERMINAL"</b> keyword or the <b>"COMMAND"</b> keyword.
The strings will be only printed in case there is an active terminal window at the moment. The terminal that runs the script will 
(well it should) not recognize any given voice command besides the <b>"TERMINAL NEW"</b> and <b>"TERMINAL SILENCE"</b> commands.

<b>Voice Command</b> | <b>'Terminal Command'</b>
:---|:---
ARGUMENT     | 'xargs'
COPY         | 'cp'
CD           | 'cd'
CLEAR        | 'clear'
DIRECTORY    | 'mkdir'
ECHO         | 'echo'
EXIT         | 'exit'
FIND         | 'find'
GIT          | 'git'
GLOBAL       | 'grep'
LESS         | 'less'
LIST         | 'ls'
LOCATE       | 'plocate'
MAN          | 'man'
MOVE         | 'mv'
NANO         | 'nano'
NEW          | 'gnome-terminal'
PIPE         | '\|'
PIPELINE     | '\|'
REMOVE       | 'rm'
SILENCE      | 'silence'
STREAM       | 'sed'
SWITCH       | 'sudo'
TAR          | 'tar'
ZIP          | 'gzip'

The following table displays the supported actions with the CTRL key. They only work when the voice command is preceded by the <b>"CONTROL"</b> keyword.

<b>Voice Command</b> | <b>Control Command</b>
:---|:---
CLEAR  |  CTRL+L
CLIP   |  CTRL+X
COPY   |  CTRL+C
CUT    |  CTRL+X
PASTE  |  CTRL+V
SAVE   |  CTRL+S
SEARCH |  CTRL+F
SELECT |  CTRL+A
UNDO   |  CTRL+Z

The following table displays the supported text outputs with the SHIFT key. The respective voice command is preceded by the <b>"SHIFT"</b> keyword.

<b>Voice Command</b> | <b>'Text Output'</b>
:---|:---
ZERO  | ')'
ONE   | '!'
TWO   | '@'
THREE | '#'
FOUR  | '$'
FIVE  | '%'
SIX   | '¨'
SEVEN | '&'
EIGHT | '*'
NINE  | '('

In addtion to the above commands, the <b>"HOLD"</b> and <b>"RELEASE"</b> keywords can be used to maintain pressed or release
the <b>"CONTROL"</b> and <b>"SHIFT"</b> keys separatedely or at the same time.

The remaining commands / voice inputs that appear in the scripts / grammar files are either experimental or will be implemented later.
# Dependencies
You basically need the following dependencies before running the script:
- A Python 3 interpreter (installation depends on the Linux Distro you are using)
- The [pynput library](https://pypi.org/project/pynput/) (same as above)
- The Julius binary as well as the related acoustic model files, configuration file and voca and grammar files

The Julius dependencies are all already present in this repo. The binary, the acoustic model files as well as the dictionary of all possible recognizable words is the latest provided by the [VoxForge project](https://www.voxforge.org/). The "`terminal.voca`" and "`terminal.grammar`" files define the set of all words that we want to recognize and the possible sentences in which they can be arranged. The remaining "`terminal.*`" files can be generated by calling the Perl script "`mkdfa.pl`" with "terminal" as its argument.
Finally, the "`terminal.jconf`" file contains all the options and high-level configurations applied to improve Julius recognition.

For more info please check [Julius' page](http://julius.osdn.jp/en_index.php) and [VoxForge's page](https://www.voxforge.org/)
# References 
"Large Vocabulary Continuous Speech Recognition Engine Julius" , i.e., Julius:
> A. Lee, T. Kawahara and K. Shikano. "Julius --- An Open Source Real-Time Large Vocabulary Recognition Engine".  In Proc. EUROSPEECH, pp.1691--1694, 2001.

> A. Lee and T. Kawahara. "Recent Development of Open-Source Speech Recognition Engine Julius" Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC), 2009.

> A. Lee and T. Kawahara: Julius v4.5 (2019) https://doi.org/10.5281/zenodo.2530395

Acoustic models and phonetic dictionary by Voxforge:
> https://www.voxforge.org/home/downloads
