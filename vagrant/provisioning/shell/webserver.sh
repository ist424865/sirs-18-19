#!/usr/bin/env bash

route del -net default >/dev/null
route add default gw 192.168.20.80 >/dev/null