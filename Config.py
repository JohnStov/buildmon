import datetime
import Missile

#Url = 'http://192.168.0.4'
#BuildType = 'HelloWorld_Build'
Url = 'http://4g5965j-dt2-s:88'
BuildType = 'ClientExams_Build'
SleepSeconds = 10
StartTime = datetime.time(8, 00)
StopTime = datetime.time(18, 00)

Targets = {
    "tribalgroup\john.stovin" : (
        ("zero", 0), # Zero/Park to know point (bottom-left)
        ("led", 1), # Turn the LED on
        ("right", 3250),
        ("up", 540),
        ("fire", 4), # Fire a full barrage of 4 missiles
        ("led", 0), # Turn the LED back off
        ("zero", 0), # Park after use for next time
    ),
    "tribalgroup\simon.bryan" : (
        ("zero", 0), 
        ("right", 4400),
        ("up", 200),
        ("fire", 4),
        ("zero", 0),
    ),
    "default" : (
        ("zero", 0),
        ("right", 5200),
        ("up", 500),
        ("pause", 5000),
        ("left", 2200),
        ("down", 500),
        ("zero", 0),
    ),
}