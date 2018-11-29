"""
Connect to hosts via telnet
"""

import telnetlib


def login(host, username, password):
    try:
        # Start connection
        tn = telnetlib.Telnet(host)
        # 'b' before converts to binary
        tn.read_until(b"login: ", 10)
        tn.write(username.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
    except EOFError:
        print("Cannot connect to host")
        return

    # Returns telnet connection
    return tn