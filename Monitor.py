from Speech import say
import HostInfo
import Config
from TeamCity import TeamCity, NoConnection, NoBuild
import Lights
import Display
import time

def initialize():
    say('Hello')
    Display.clear()
    Display.write("     Hello!     ")

teamCity = None
currentBuildId = None
lastBuildId = None

def set_state(build):
    global teamCity, lastBuildId

    if lastBuildId == build['id']:
        return
    lastBuildId = build['id']

    if teamCity.build_failed(build):
        say ('build {0} failed'.format(build['number']))
        Display.rgb(255, 0, 0)
        Lights.broken_build()
    else:
        Display.rgb(0, 255, 0)
        say ('build {0} succeeded'.format(build['number']))
        Lights.build_good()

def connect():
    global teamCity

    while teamCity == None:
        try:
            teamCity = TeamCity(Config.Url, Config.BuildType)
        except NoConnection:
            Display.set_cursor_position(0, 1)
            Display.write(' No Connection ')
            say('failed to connect to server at {0}'.format(Config.Url))
        except NoBuild:
            Display.set_cursor_position(0, 1)
            Display.write('Bad BuildType')
            say('could not find build type {0}'.format(Config.BuildType))
        
        if teamCity == None:
            say('trying again in one minute')
            time.sleep(60)
        else:
            Display.set_cursor_position(0, 1)
            Display.write('   Connected     ')

def disconnect():
    global teamCity

    if teamCity:
        teamCity.close()
        teamCity = None

def report_status():
    global currentBuildId
    global teamCity

    build = teamCity.get_latest_build()
    if teamCity.build_finished(build):
        set_state(build)
    else:
        if currentBuildId == build['id']:
            return
        else:
            currentBuildId = build['id']
            say('building')

def check_connection():
    ip = None
    while (ip == None):
        try:
            ip = HostInfo.getIpAddress()
            say('running at ip address {0}'.format(ip))
            Display.set_cursor_position(0,0)
            Display.write(ip)
        except Exception:
            Display.set_cursor_position(0, 1)
            Display.write(' No Connection ')
            say('failed to connect to network')
            say('trying again in one minute')
            time.sleep(60)


if __name__ == '__main__':
    initialize()
    check_connection()

    say('connecting to server at {0}'.format(Config.Url))
    say('monitoring build {0}'.format(Config.BuildType))
    
    while True:
        connect()
        report_status()
        disconnect()
        time.sleep(Config.SleepSeconds)
