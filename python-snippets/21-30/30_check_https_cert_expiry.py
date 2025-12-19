import socket
import ssl
import time
from datetime import datetime, timezone

def check_https_cert_expiry(hostname, port=443, timeout=5):
    ctx = ssl.create_default_context()

    with socket.create_connection((hostname, port), timeout=timeout) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()  # dict with fields like "notAfter"
            not_after = cert.get("notAfter")
            if not not_after:
                raise RuntimeError("Could not read certificate expiry (notAfter missing).")

            # Convert to epoch seconds using stdlib helper
            expiry_epoch = ssl.cert_time_to_seconds(not_after)
            now_epoch = time.time()
            days_left = int((expiry_epoch - now_epoch) // 86400)

            expiry_dt = datetime.fromtimestamp(expiry_epoch, tz=timezone.utc)
            return expiry_dt, days_left

if __name__ == "__main__":
    host = input("Hostname (e.g., example.com): ").strip()
    expiry_dt, days_left = check_https_cert_expiry(host)
    print(f"Expires at (UTC): {expiry_dt.isoformat()}")
    print(f"Days left: {days_left}")
