#!/usr/bin/python
import psutil


def memorypercent():
    return str(psutil.virtual_memory().percent)
