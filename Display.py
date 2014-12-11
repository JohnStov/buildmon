import Platform

if Platform.is_raspberrypi():
    from dot3k import lcd, backlight

def clear():
    if Platform.is_raspberrypi():
        lcd.clear()

def write(str):
    if Platform.is_raspberrypi():
        lcd.write(str)
    else:
        print str

def set_cursor_position(x, y):
    if Platform.is_raspberrypi():
        lcd.set_cursor_position(x, y)

def set_graph(intensity):
    if Platform.is_raspberrypi():
        backlight.set_graph(intensity)

def rgb(r, g, b):
    if Platform.is_raspberrypi():
        backlight.rgb(r, g, b)

def hue(value):
    if Platform.is_raspberrypi():
        backlight.hue(value)

def sweep(value):
    if Platform.is_raspberrypi():
        backlight.sweep(value)
