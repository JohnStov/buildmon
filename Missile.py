import Platform

if Platform.is_raspberrypi():
    import usb.core

    device = usb.core.find(idVendor=0x2123, idProduct=0x1010)
    try:
        device.detach_kernel_driver(0)
    except Exception:
        pass

import time

Down  = 0x01
Up    = 0x02
Left  = 0x04
Right = 0x08
Fire  = 0x10
Stop  = 0x20

def send_cmd(cmd):
    if Platform.is_raspberrypi() and device != None:
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    else:
        print "sending usb command {0}".format(cmd)
    
def led(cmd):
    if Platform.is_raspberrypi() and device != None:
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    else:
        print "sending missile led state {0}".format(cmd)

led(0)

def send_move(cmd, duration_ms):
    send_cmd(cmd)
    time.sleep(duration_ms / 1000.0)
    send_cmd(Stop)

def run_command(command, value):
    command = command.lower()
    if command == "right":
        send_move(Right, value)
    elif command == "left":
        send_move(Left, value)
    elif command == "up":
        send_move(Up, value)
    elif command == "down":
        send_move(Down, value)
    elif command == "zero" or command == "park" or command == "reset":
        # Move to bottom-left
        send_move(Down, 2000)
        send_move(Left, 8000)
    elif command == "pause" or command == "sleep":
        time.sleep(value / 1000.0)
    elif command == "led":
        if value == 0:
            led(0x00)
        else:
            led(0x01)
    elif command == "fire" or command == "shoot":
        if value < 1 or value > 4:
            value = 1
        # Stabilize prior to the shot, then allow for reload time after.
        time.sleep(0.5)
        for i in range(value):
            send_cmd(Fire)
            time.sleep(4.5)
    else:
        print "Error: Unknown command: '%s'" % command


def run_command_set(commands):
    for cmd, value in commands:
        run_command(cmd, value)

if __name__ == "__main__":
    led(0)
    time.sleep(1)
    led(1)
    time.sleep(1)
    led(0)
    send_move(Left, 1000)
    send_cmd(Fire)
