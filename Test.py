from Speech import say
import time
from dot3k import backlight, lcd
import Lights

def test_lights():
    say('Testing lights')
    lcd.set_cursor_position(0,2)
    lcd.write('Lights          ')

    say('Lamp 0 on')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 0 On       ')
    Lights.set_lamp(0, 1)
    time.sleep(3)

    say('Lamp 1 on')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 1 On       ')
    Lights.set_lamp(1, 1)
    time.sleep(3)

    say('Lamp 2 on')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 2 On       ')
    Lights.set_lamp(2, 1)
    time.sleep(3)

    say('Lamp 3 on')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 3 On      ')
    Lights.set_lamp(3, 1)
    time.sleep(3)

    say('Lamp 0 off')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 0 Off     ')
    Lights.set_lamp(0, 0)

    say('Lamp 1 off')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 1 Off     ')
    Lights.set_lamp(1, 0)
 
    say('Lamp 2 off')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 2 Off     ')
    Lights.set_lamp(2, 0)

    say('Lamp 3 off')
    lcd.set_cursor_position(0,2)
    lcd.write('Lamp 3 Off')
    Lights.set_lamp(3, 0)

    lcd.set_cursor_position(0,2)
    lcd.write('                ')

def test_bargraph():
    say('testing bargraph')
    lcd.set_cursor_position(0,2)
    lcd.write('Bargraph        ')
    for intensity in range (0,100):
        backlight.set_graph(intensity/100.0)
        time.sleep(.01)
    for intensity in range (100,0,-1):
        backlight.set_graph(intensity/100.0)
        time.sleep(.01)
    lcd.set_cursor_position(0,2)
    lcd.write('                ')

def test_backlight():
    say('testing backlight')
    lcd.set_cursor_position(0,2)
    lcd.write('Backlight       ')
    backlight.rgb(255,0,0)
    time.sleep(1)
    backlight.rgb(0,255,0)
    time.sleep(1)
    backlight.rgb(0,0,255)
    time.sleep(1)
    for i in range(0, 360):
        backlight.hue(i/360.0)
        time.sleep(0.01)
    for i in range(0, 360):
        backlight.sweep(i/360.0)
        time.sleep(0.01)

    backlight.rgb(255,255,255)
    lcd.set_cursor_position(0,2)
    lcd.write('                ')
    
def test_all():
    test_backlight()
    test_bargraph()
    test_lights()

if __name__ == "__main__":
    test_all()
