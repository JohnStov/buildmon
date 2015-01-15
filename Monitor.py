from Speech import say
import HostInfo
import Config
from TeamCity import TeamCity, NoConnection, NoBuild
import Lights
import Display
import datetime
import time
import Missile

def initialize():
    Display.rgb(255, 255, 255)
    say('Hello')
    Display.clear()
    Display.write("     Hello!     ")

def go_to_sleep():
    say('Goodnight')
    Display.clear()
    Display.rgb(0, 0, 0)
    Lights.all_off()

teamCity = None
currentBuildId = None
lastBuildId = None
buildBreakers = None
displayOn = True

def target_missile(name):
    print "trying to target {0}".format(name)
    if Config.Targets.has_key(name):
        print "targetting {0}".format(name)
        Missile.run_command_set(Config.Targets[name])
    else:
        print "targeting default"
        Missile.run_command_set(Config.Targets['default'])

def display_state(build):
    global teamCity, lastBuildId, buildBreakers

    if lastBuildId == build['id']:
        return
    lastBuildId = build['id']

    if teamCity.build_failed(build):
        failedTests = len(teamCity.get_failed_tests(build))
        if failedTests > 0:
            say('build {0}, {1} tests failed'.format(build['number'], failedTests))
            Display.rgb(255, 255, 0)
            Lights.broken_test()
        else:
            say ('build {0} failed'.format(build['number']))
            Display.rgb(255, 0, 0)
            Lights.broken_build()
        if buildBreakers == None:
            buildBreakers = teamCity.get_checkins(build)
            for breaker in buildBreakers:
                target_missile(breaker.lower())
            for breaker in buildBreakers:
                say ('{0} broke the build'.format(breaker))
    else:
        Display.rgb(0, 255, 0)
        say ('build {0} succeeded'.format(build['number']))
        Lights.build_good()
        if buildBreakers != None:
            buildBreakers = None
            for fixer in teamCity.get_checkins(build):
                say ('{0} fixed the build'.format(fixer))

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
        display_state(build)
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

def check_time():
    global displayOn

    now = datetime.datetime.now().time()
    if now >= Config.StartTime and now <= Config.StopTime:
        if displayOn == False:
            initialize()
        displayOn = True
    else:
        if displayOn == True:
            go_to_sleep()
        displayOn = False
    return displayOn


if __name__ == '__main__':
    initialize()
    check_connection()

    say('connecting to server at {0}'.format(Config.Url))
    say('monitoring build {0}'.format(Config.BuildType))
    
    while True:
        if check_time():
            connect()
            report_status()
            disconnect()
        
        time.sleep(Config.SleepSeconds)
