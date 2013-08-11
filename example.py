from time import sleep
from xdotool.keys import ctrl, shift, _t, Enter
from xdotool.commands import *

do(ctrl+shift+_t)
sleep(2)
do('cd ~/projects/example', Enter)
do('. venv/bin/activate', Enter)