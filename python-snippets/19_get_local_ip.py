import socket

# Connect to external UDP endpoint (doesn't send data)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))  # Google DNS, any external host:port
local_ip = sock.getsockname()[0]
sock.close()

print(f"Local IP: {local_ip}")
