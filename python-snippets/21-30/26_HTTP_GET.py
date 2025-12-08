import requests

def simple_http_get(url, timeout=10):
    """
    Make a simple HTTP GET request and display basic response info.
    """
    try:
        # Send GET request
        response = requests.get(url, timeout=timeout)
        
        # Display results
        print(f"URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'N/A')}")
        print(f"Content Length: {len(response.content)} bytes")
        print(f"\nFirst 500 characters of response:\n{response.text[:500]}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    target_url = input("Enter URL (e.g., https://example.com): ").strip()
    simple_http_get(target_url)
