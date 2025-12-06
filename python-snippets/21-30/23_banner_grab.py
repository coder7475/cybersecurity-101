import socket

def grab_banner(host, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        
        # Send HTTP HEAD request
        request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        sock.send(request.encode())
        
        # Receive response (first 1024 bytes)
        banner = sock.recv(1024).decode(errors='ignore')
        sock.close()
        
        return banner
    except Exception as e:
        return f"Error: {e}"

# Example usage
target = "scanme.nmap.org"
print(f"Banner from {target}:80")
print("=" * 50)
print(grab_banner(target, 80))
