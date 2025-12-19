import requests

def login_and_fetch(login_url, protected_url, username, password, timeout=10):
    # Session keeps cookies between requests (common for login flows)
    with requests.Session() as s:
        payload = {
            "username": username,
            "password": password,
        }

        # Many sites expect form-encoded login data (data=...), not JSON.
        login_resp = s.post(login_url, data=payload, timeout=timeout, allow_redirects=True)

        print(f"Login status: {login_resp.status_code}")
        print(f"Final login URL: {login_resp.url}")

        # After login, try a page that requires authentication
        protected_resp = s.get(protected_url, timeout=timeout, allow_redirects=True)
        print(f"Protected page status: {protected_resp.status_code}")

        # Show a small preview so you can confirm you're authenticated
        print(protected_resp.text[:500])

if __name__ == "__main__":
    login_url = input("Login URL (e.g., https://site.com/login): ").strip()
    protected_url = input("Protected URL (e.g., https://site.com/dashboard): ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    login_and_fetch(login_url, protected_url, username, password)
