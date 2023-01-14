import pypresence
from pypresence import Presence
import time
import psutil

def grabCPU(): #function to grab cpu usage percent as a string
    return str(psutil.cpu_percent()) + "%"

def grabRAM(): #function to grab ram usage percent as a string
    return str(psutil.virtual_memory().percent) + "%"

def readClientID(): #function to open client_id.txt and read whats inside, then return it
    with open("client_id.txt") as x:
        clientID = x.readline().strip()
    return clientID

client_id = readClientID()  #put your client id in client_id.txt
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop
print("RPC connected successfully ^_^")

while True:  # The presence will stay on as long as the program is running (in this case, infinitely)
    RPC.update(state = "RAM Usage: " + grabRAM(), details="CPU Usage: " + grabCPU()) # Updates our presence
    time.sleep(15) # Can only update rich presence every 15 seconds
