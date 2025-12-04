import base64

data = input("Text: ").encode()
encode = base64.b64encode(data)

print(encode.decode())