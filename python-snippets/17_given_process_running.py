import subprocess

def is_process_running(name):
    result = subprocess.run(["pgrep", "-f", name], capture_output=True)
    return result.returncode == 0

# Examples
print("Apache running?", is_process_running("apache2"))
print("SSH running?", is_process_running("sshd"))
print("Node running:", is_process_running("node"))
