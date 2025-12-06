# Check password strength
pwd = input("Password: ")

score = 1 if len(pwd) >= 8 else 0

for c in pwd:
    if c.isdigit():
        score += 1
    elif c.isupper():
        score += 1
    elif not c.isalnum():
        score += 1

print("Strength (0-4): ", score)