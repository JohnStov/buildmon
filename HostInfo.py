import socket

def getIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com',80))
    result = s.getsockname()[0]
    s.close()
    return result
