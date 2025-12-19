import requests

def fuzz_query_param(base_url, param_name="q", timeout=10):
    payloads = [
        "test",
        "'",
        "\"",
        "<script>alert(1)</script>",
        "../",
        " OR 1=1 --",
    ]

    with requests.Session() as s:
        for payload in payloads:
            try:
                r = s.get(base_url, params={param_name: payload}, timeout=timeout, allow_redirects=False)
                length = len(r.content)
                print(f"{r.status_code} len={length}  {r.url}")
            except requests.RequestException as e:
                print(f"ERROR payload={payload!r}: {e}")

if __name__ == "__main__":
    url = input("Target URL (e.g., https://example.com/search): ").strip()
    name = input("Parameter name (default q): ").strip() or "q"
    fuzz_query_param(url, name)
