import socket

def is_port_open(host, port):
    # Create socket with ipv4 addr with tcp port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3) # 3 second timeout

    result = sock.connect_ex((host, port))

    sock.close()

    return result == 0

# Examples
print("Local port 80 open?", is_port_open("127.0.0.1", 80))
print("Local SSH open?", is_port_open("127.0.0.1", 22))
print("Target 443?", is_port_open("scanme.nmap.org", 443))
print("Target 80?", is_port_open("scanme.nmap.org", 80))

