from Speech import say
import HostInfo
from dot3k import lcd
import Config
from TeamCity import TeamCity
import Lights

def initialize():
    say('Hello')
    lcd.clear()
    lcd.write("     Hello!     ")

def set_state(teamCity, build):
    if teamCity.build_failed(build):
        say ('the build is broken')
        Lights.broken_build()
    else:
        say ('the build succeeded')
        Lights.build_good()

if __name__ == '__main__':
    initialize()

    ip = HostInfo.getIpAddress()
    say('running at ip address {0}'.format(ip))
    lcd.set_cursor_position(0,0)
    lcd.write(ip)

    say('connecting to server at {0}'.format(Config.Url))
    teamCity = TeamCity(Config.Url, Config.BuildType)
    
    while True:
        latest_build = teamCity.get_latest_build()
        if teamCity.build_finished(latest_build):
            set_state(latest_build)
        time.sleep(Config.SleepSeconds)
