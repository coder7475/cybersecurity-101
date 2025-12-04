import base64

b = input("Base64: ").encode()

print("Decode: ", base64.b64decode(b).decode(errors="ignore"))
