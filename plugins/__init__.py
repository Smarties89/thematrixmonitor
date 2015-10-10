#!/usr/bin/python

from cpu import cpu
from network import network
from memorypercent import memorypercent
from processes import processes

# This is the active windows.
columns = [
    cpu,
    network,
    memorypercent,
    processes
]

