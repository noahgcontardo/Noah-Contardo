def GCD(a, b):
    while True:
        if a == 0:
            return b            
        c = b % a
        b = a
        a = c

def main():
    inputty_a = int(input("please provide bigger value a to calculate GCD: "))
    inputty_b = int(input("please provide smaller value b to calculate GCD: "))
    if inputty_a > inputty_b:
        x = GCD(inputty_a, inputty_b)
        print(x)
    elif inputty_b > inputty_a:
        x = GCD(inputty_b, inputty_a)
        print(x)
    elif inputty_a == inputty_b:
        print("lol its the same number")
main()
