import random 
start = 0
while True:
    start = start + random.randrange(1, 10)
    print(start)
    yn = input("keep going (y/n?)")
    if yn.startswith("n") or yn.startswith("N"):
        break
    