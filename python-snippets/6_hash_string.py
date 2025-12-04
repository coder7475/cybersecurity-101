import hashlib

# User Input
data = input("Text: ").encode()

# Hashed
hashed = hashlib.md5(data).hexdigest()
hashed2 = hashlib.sha256(data).hexdigest()

# Output
print(f"MD5: {hashed}")
print(f"SHA256: {hashed2}")