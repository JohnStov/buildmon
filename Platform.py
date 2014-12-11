import os

def is_windows():
    return os.name == 'nt'

def is_linux():
    return os.name =='posix'

def is_raspberrypi():
    return is_linux() and os.uname()[1] == 'raspberrypi'