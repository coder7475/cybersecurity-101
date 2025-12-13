import requests

def check_common_paths(base_url: str, paths: list[str], timeout=5):
    """
    check which common paths exits on a web server
    """
    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url

    print(f"Checking paths on: {base_url}\n")

    for path in paths:
        url = base_url.rstrip("/") + "/" + path.lstrip("/")
        try:
            response = requests.get(url, timeout=timeout, allow_redirects=True)
            
            status = response.status_code

            if 200 <= status < 300:
                print(f"[+] Found: {url} (Status: {status})")
            elif 300 <= status < 400:
                print(f"[+] REDIRECT: {url} (Status: {status})")
            else:
                print(f"[-] Not Found: {url} (Status: {status})")
             

        except requests.RequestException as e:
            print(f"[!] ERROR: {url} - {e}")


if __name__ == "__main__":
    common_paths = [
        "/",
        "/admin",
        "/login",
        "/robots.txt",
        "/.git/",
        "/phpinfo.php",
        "/wp-admin/",
        "/api/",
        "/config/",
    ]

    target = input("Enter the target URL (e.g. example.com): ").strip()

    check_common_paths(target, common_paths)

