import subprocess

# Run ps sorted by CPU usage (descending)
result = subprocess.run(["ps", "aux", "--sort=-%cpu"], capture_output=True, text=True)
processes = result.stdout.strip().split("\n")

print(f"{'PID':<8} {'USER':<10} {'CPU':>5} {'MEM':>5} COMMAND")
print("-" * 60)

for line in processes[1:11]:  # Skip header and take top 10
    parts = line.split(maxsplit=10)
    if len(parts) >= 11:
        user = parts[0]
        pid = parts[1]
        cpu = parts[2]
        mem = parts[3]
        command = parts[10][:30]  # truncate if too long
        print(f"{pid:<8} {user:<10} {cpu:>5} {mem:>5} {command}")
