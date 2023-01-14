import pypresence
from pypresence import Presence
import time
import psutil

def grabCPU():
    return str(psutil.cpu_percent()) + "%" # why is this so dogshit lmao

def grabRAM():
    return str(psutil.virtual_memory().percent) + "%"

def readClientID():
    with open("client_id.txt") as x:
        clientID = x.readline().strip()
    return clientID

client_id = readClientID()  # Put your Client ID in client_id.txt
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    RPC.update(state = "RAM Usage: " + grabRAM(), details="CPU Usage: " + grabCPU()) # Updates our presence
    time.sleep(15) # Can only update rich presence every 15 seconds
