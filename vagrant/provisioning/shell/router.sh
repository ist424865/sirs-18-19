#!/usr/bin/env bash

modprobe iptable_nat
echo 1 | sudo dd of=/proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth1 -j ACCEPT