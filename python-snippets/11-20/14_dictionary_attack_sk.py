# Offline dictionary attack (string compare demo)
target = "secret123"
wordlist = ["password", "admin", "secret", "secret123", "letmein"]

for word in wordlist:
    if word == target:
        print(f"Cracked: {word}")
        break
else:
    print("Not in wordlist")
