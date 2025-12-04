import hashlib

path = './../bin/file.bin'

# Create a new SHA256 hash object.
h = hashlib.sha256()

# Open the file in binary read mode ('rb').
with open(path, "rb") as f:
    """
    Read the file in chunks to handle large files efficiently without
    consuming too much memory. 4096 bytes (4KB) is a common chunk size.
    The iter() function with two arguments will call f.read(4096)
    repeatedly until it returns an empty byte string (b""), which marks the end of the file.
    """
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)

# Print the final hash digest in hexadecimal format.
print(f"SHA256 Hash: {h.hexdigest()}")