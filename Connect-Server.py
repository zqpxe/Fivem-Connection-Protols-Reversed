"""
This script shows the attempt when your fivem client connects to a server
It misses some arguments, which I cannot possibly generate alone. 

Special tokens and additional data that are not included or explained here.
Note: Misuse of ths script may actually cause you more harm than good.
"""

import requests

server_address = ""  # Put the server IP
server_port = ""     # Put the server Port (eg. 30120)

# The URL the client creates under the process of joining
url = f"http://{server_address}:{server_port}/client"

# Headers for the request (From the client too)
headers = {
    "Host": f"{server_address}:{server_port}",
    "User-Agent": "CitizenFX/1",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
}

# Data payload for the request (Also from the client, who all are needed)
data = {
    "method": "initConnect", 
    "gameBuild": "",       # Replace with the game build number
    "gameName": "gta5",        # Just the type of game 
    "guid": "",            # Replace with the GUID
    "name": "",            # Replace with the desired player name
    "protocol": "12",      # Protocol version
    "cfxTicket2": "",      # Replace with a valid token
    "cfxTicket": ""        # Replace with a valid token
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")

# Note: Automating token generation or retrieving the rest of the right arguments is not here. 
# If you figure out a method to do so, let me know asap!
