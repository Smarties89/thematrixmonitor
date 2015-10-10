#!/usr/bin/python
import psutil


def cpu():
    return str(psutil.cpu_percent())
