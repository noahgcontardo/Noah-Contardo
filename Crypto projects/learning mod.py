a = 1331
b = 1001
def GCD(a, b):
    while True:
        if a == 0:
            print(b)
            return b
            
        c = b % a
        b = a
        a = c

GCD(a,b)