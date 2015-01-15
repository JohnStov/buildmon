import Platform
import time
from threading import Thread

if Platform.is_raspberrypi():
    from dot3k import lcd, backlight

scrollThread = None

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

class Scroller(Thread):
    def __init__(self, str, line, timeout=0):
        Thread.__init__(self)
        self.str = str
        self.line = line
        self.timeout = timeout
        self.running = True

    def run(self):
        now = time.time()
        stoptime = now + self.timeout

        if self.line < 0 or self.line >= 3:
            return

        set_cursor_position(0, self.line)
        write('                ')

        if len(self.str) <= 16:
            set_cursor_position(0, line)
            write(self.str)
            if self.timeout > 0:
                time.sleep(self.timeout)
                set_cursor_position(0, self.line)
                write('                ')

        scroll_str = self.str + ' '
        while(self.running):
            for x in range(0, len(scroll_str)):
                now = time.time()
                if self.timeout > 0 and now > stoptime:
                    self.stop()

                if self.running == False:
                    break

                end1 = min(x+17, len(scroll_str)+1)
                end2 = max(0, 17-(end1-x))
                display_str = scroll_str[x:end1] + scroll_str[0:end2]
                write(display_str)
                time.sleep(0.2)

        set_cursor_position(0, self.line)
        write('                ')

    def stop(self):
        self.running = False

def scroll(str, line, timeout=0):
    global scrollThread
    
    stop_scroll()
    scrollThread = Scroller(str, line, timeout)
    scrollThread.start()

def stop_scroll():
    global scrollThread

    if scrollThread != None:
        scrollThread.stop()
        scrollThread.join()
        scrollThread = None

if __name__ == '__main__':
    scroll("This is a long message", 0, 5)
    time.sleep(10)
    scroll("This is a longer message", 0)
    time.sleep(10)
    stop_scroll()

