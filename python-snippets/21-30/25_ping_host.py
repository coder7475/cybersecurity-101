import subprocess

def ping_host(host):
    # ping 3 times with 2s timeout
    result = subprocess.run(
        ["ping", "-c", "3", "-W", "2", host],
        capture_output=True,
        text=True
    )

    return result.returncode == 0

# Usage
examples = ["scanme.nmap.org", "8.8.8.8", "localhost", "noexistent.fake"]

print("Ping results: ")
print("="*30)

for target in examples:
    status = "UP" if ping_host(target) else "DOWN"
    print(f"{target:20} -> {status}")



