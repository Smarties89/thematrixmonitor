#!/usr/bin/python


import psutil

netconns = []


def network():
    global netconns
    if not netconns:
        netconns = psutil.net_connections()
        if not netconns:
            return "Empty"

    result = netconns.pop()

    while result.laddr[0].startswith("::") or result.status == "NONE":
        result = netconns.pop()
    if result.status == "ESTABLISHED":
        return "{} {:16} {:16}".format(
            result.status[0],
            result.laddr[0]+":"+str(result.laddr[1]),
            result.raddr[0]+":"+str(result.raddr[1]))
    elif result.status == "LISTEN":
        if result.laddr[0] == "127.0.0.1":
            # We are not interested in local running services.
            return network()

        return "{} {:16} {:16}".format(
            result.status[0],
            result.laddr[0],
            "NA")
    else:
        return "ERROR IN network()"
