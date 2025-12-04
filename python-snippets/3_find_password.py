with open("./../data/config.txt", 'r') as f:
    for line in f:
        if "password" in line.lower():
            print(line.strip())