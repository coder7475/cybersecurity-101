import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Faster timeout for range scans
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Scan well-known ports 1-1024
target = "scanme.nmap.org"
open_ports = []

print(f"Scanning {target} ports 1-1024...")
print("=" * 40)

for port in range(1, 1025):
    if scan_port(target, port):
        print(f"[+] Port {port} OPEN")
        open_ports.append(port)

print("=" * 40)
print(f"\nFound {len(open_ports)} open ports: {open_ports}")
