import string, secrets

chars = string.ascii_letters + string.digits + string.punctuation

print("Password Generator")

length = input("Length: ")

password = "".join(secrets.choice(chars) for _ in range(int(length)))

print("--"*40)
print(f"Generated Password: {password}")
print("--"*40)