import subprocess
from xdotool.keys import Key, slash


def do_key(key):
    subprocess.call(["xdotool", "key", key])


def do_type(text):
    lines = str(text).split('/')
    for line in lines[:-1]:
        subprocess.call(["xdotool", "type", line])
        do_key(slash)
    subprocess.call(["xdotool", "type", lines[-1]])


def do(*args):
    for arg in args:
        if isinstance(arg, Key):
            do_key(arg)
        else:
            do_type(arg)