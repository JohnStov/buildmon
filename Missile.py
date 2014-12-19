import usb.core
import time

device = usb.core.find(idVendor=0x2123, idProduct=0x1010)
try:
    device.detach_kernel_driver(0)
except Exception:
    pass

Down  = 0x01
Up    = 0x02
Left  = 0x04
Right = 0x08
Fire  = 0x10
Stop  = 0x20

def send_cmd(cmd):
    device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    

def led(cmd):
    device.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def send_move(cmd, duration_ms):
    send_cmd(cmd)
    time.sleep(duration_ms/1000.0)
    send_cmd(Stop)

if __name__ == "__main__":
    led(0)
    time.sleep(1)
    led(1)
    time.sleep(1)
    led(0)
    send_move(Left, 1000)
    send_cmd(Fire)
