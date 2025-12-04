## Networking & Recon

```bash
nmap -sC -sV -p- target          # Full scan with scripts & versions
netstat -tuln                    # Listening TCP/UDP ports
ss -tuln                         # Modern netstat (listening ports)
ip addr show      # or ip a      # Show IPs and interfaces
arp -a                           # ARP table (IP ↔ MAC)
dig example.com A                # DNS A record lookup
whois example.com                # WHOIS info for domain
curl -I http://target            # HTTP headers (HEAD request)
traceroute 8.8.8.8               # Show network path (hops)
tcpdump -i eth0 -w capture.pcap  # Capture packets to pcap
ifconfig           # or ip link  # Interface status
ip route                         # Routing table
lsof -i :80                      # Process using port 80
masscan --rate=1000 80,443 10.0.0.0/24  # Fast scan (lab only)
dnsenum target.com               # DNS enumeration
```

## Files & Directories

```bash
ls -la                           # Long list incl. hidden files
find /etc -name "*.conf" 2>/dev/null   # Find config files
grep -r "password" /etc         # Search recursively for “password”
cat file.txt                     # Show file contents
tail -f /var/log/auth.log        # Follow log in real time
strings /bin/ls                  # Printable strings from binary
file suspicious.exe              # Detect file type
xxd file.bin                     # Hex dump
chmod 755 script.sh              # Set rwx/r-x/r-x
chown root:root file             # Change owner to root:root
du -sh /var/log                 # Disk usage summary (human)
```

## Processes & System

```bash
ps aux | grep apache             # List processes matching apache
top                              # Live process monitor
htop                             # Enhanced top (if installed)
kill -9 1234                     # Force kill PID 1234
pkill -f nginx                   # Kill processes matching “nginx”
systemctl status nginx           # Service status
journalctl -u ssh -f             # Follow SSH service logs
df -h                            # Disk usage for filesystems
free -h                          # Memory usage
uptime                           # Uptime + load average
w                                # Who is logged in, what they run
```

## Users & Privileges

```bash
id                               # Current UID, GID, groups
sudo -l                          # Sudo rights for this user
passwd                           # Change current user password
useradd -m hacker                # Add user with home dir
groups                           # Groups of current user
```

## Forensics & Advanced

```bash
history | grep ssh               # Shell history filtered by ssh
last                             # Recent logins & reboots
dmesg | grep error               # Kernel messages with “error”
lsmod                            # Loaded kernel modules
iptables -L -n -v                # Firewall rules (legacy iptables)
crontab -l                       # User’s cron jobs
env | grep PASS                  # Env vars with “PASS”
mount | grep noexec              # Mounts with noexec flag
dmidecode --type bios            # BIOS/firmware info
lscpu                            # CPU info
```

## Handy aliases (add to `~/.bashrc`)

```bash
alias scan='nmap -sC -sV -p-'
alias cb='xclip -sel clip'
alias ports='ss -tuln'
alias myip='ip addr show'
alias histssh="history | grep ssh"
```

Source it after editing:

```bash
source ~/.bashrc
```