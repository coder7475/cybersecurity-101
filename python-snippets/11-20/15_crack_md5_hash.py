import hashlib

target_hash = "5ebe2294ecd0e0f08eab7690d2a6ee69"  # MD5("secret123")
wordlist = ["password", "admin", "secret", "secret123", "letmein"]

for word in wordlist:
    h = hashlib.md5(word.encode()).hexdigest()
    if h == target_hash:
        print(f"Cracked: {word} -> {h}")
        break
else:
    print("Not in wordlist")
