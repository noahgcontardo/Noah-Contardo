
def GCD(value_a, value_b):
    
    if value_a == 0:
        return value_b
    return GCD(value_b % value_a, value_a)


def main():
    a = int(input('please provide a value for the first number: '))
    b = int(input('please provide a value for the second number: '))
    g = GCD(a, b)
    print(f"the gcd is {g}")

main()