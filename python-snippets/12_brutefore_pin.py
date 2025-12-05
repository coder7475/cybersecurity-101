target = '0421'

for i in range(10000):
    guess = f"{i:04d}"
    if guess == target:
        print("Found: ", guess)
        break