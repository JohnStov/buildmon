from Speech import say
import time
import Display
import Lights

def test_lights():
    say('Testing lights')
    Display.set_cursor_position(0,2)
    Display.write('Lights          ')

    say('Lamp 0 on')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 0 On       ')
    Lights.set_lamp(0, 1)
    time.sleep(3)

    say('Lamp 1 on')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 1 On       ')
    Lights.set_lamp(1, 1)
    time.sleep(3)

    say('Lamp 2 on')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 2 On       ')
    Lights.set_lamp(2, 1)
    time.sleep(3)

    say('Lamp 3 on')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 3 On      ')
    Lights.set_lamp(3, 1)
    time.sleep(3)

    say('Lamp 0 off')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 0 Off     ')
    Lights.set_lamp(0, 0)

    say('Lamp 1 off')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 1 Off     ')
    Lights.set_lamp(1, 0)
 
    say('Lamp 2 off')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 2 Off     ')
    Lights.set_lamp(2, 0)

    say('Lamp 3 off')
    Display.set_cursor_position(0,2)
    Display.write('Lamp 3 Off')
    Lights.set_lamp(3, 0)

    Display.set_cursor_position(0,2)
    Display.write('                ')

def test_bargraph():
    say('testing bargraph')
    Display.set_cursor_position(0,2)
    Display.write('Bargraph        ')
    for intensity in range (0,100):
        Display.set_graph(intensity/100.0)
        time.sleep(.01)
    for intensity in range (100,0,-1):
        Display.set_graph(intensity/100.0)
        time.sleep(.01)
    Display.set_cursor_position(0,2)
    Display.write('                ')

def test_backlight():
    say('testing backlight')
    Display.set_cursor_position(0,2)
    Display.write('Backlight       ')
    Display.rgb(255,0,0)
    time.sleep(1)
    Display.rgb(0,255,0)
    time.sleep(1)
    Display.rgb(0,0,255)
    time.sleep(1)
    for i in range(0, 360):
        Display.hue(i/360.0)
        time.sleep(0.01)
    for i in range(0, 360):
        Display.sweep(i/360.0)
        time.sleep(0.01)

    Display.rgb(255,255,255)
    Display.set_cursor_position(0,2)
    Display.write('                ')
    
def test_all():
    test_backlight()
    test_bargraph()
    test_lights()

if __name__ == "__main__":
    test_all()
