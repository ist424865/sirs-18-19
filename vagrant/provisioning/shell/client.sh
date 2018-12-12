#!/usr/bin/env bash

ifconfig eth0 down
route del -net default >/dev/null
route add default gw 192.168.10.80 >/dev/null