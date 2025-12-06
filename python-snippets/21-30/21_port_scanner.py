import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Scan common ports
target = "scanme.nmap.org"  # Legal target for practice
common_ports = [21, 22, 23, 80, 443, 3306, 3389, 8080]

print(f"Scanning {target}...")
print("=" * 40)

for port in common_ports:
    if scan_port(target, port):
        print(f"[+] Port {port:5} OPEN")
    else:
        print(f"[-] Port {port:5} closed")

print("=" * 40)
