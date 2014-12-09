from Speech import say
import HostInfo
from dot3k import lcd
import Test

def initialize():
    say('Hello')
    lcd.clear()
    lcd.write("     Hello!     ")

if __name__ == '__main__':
    initialize()

    Test.test_all()

    ip = HostInfo.getIpAddress()
    say('running at ip address {0}'.format(ip))
    lcd.set_cursor_position(0,1)
    lcd.write(ip)
