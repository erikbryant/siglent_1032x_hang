# Running this script causes a Siglent 1032X function generator to hang. No keys
# on its front respond. No socket communication works. Each of these three
# commands trigger the hang.
#   SYST:COMM:LAN:IPAD
#   SYST:COMM:LAN:SMAS
#   SYST:COMM:LAN:GAT

import socket
import sys

try:
    ip_addr = sys.argv[1]
    port = int(sys.argv[2])
except Exception as err:
    print(f"Usage: {sys.argv[0]} ip_addr port")
    sys.exit(1)

device = socket.create_connection((ip_addr, port))
device.send(str.encode("SYST:COMM:LAN:GAT\n"))
device.close()
