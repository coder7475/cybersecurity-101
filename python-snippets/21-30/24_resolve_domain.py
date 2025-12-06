import socket

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        return f"Error: {e}"

# Examples
domains = ["google.com", "scanme.nmap.org", "localhost", "invalid.fake.domain"]

print("Domain → IP Resolution")
print("=" * 50)

for domain in domains:
    ip = resolve_domain(domain)
    print(f"{domain:30} → {ip}")
