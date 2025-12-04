import hashlib

def sha256(path):
    """
    Calculate the SHA-256 hash of a file at the given path.
    Returns the hexadecimal digest string.
    """
    h = hashlib.sha256()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)

    return h.hexdigest()


path = './../bin/file.bin'
path1 = './../bin/file1.bin'
path2 = './../bin/file2.bin'

print(sha256(path) == sha256(path1)) # True
print(sha256(path1) == sha256(path2)) # False
