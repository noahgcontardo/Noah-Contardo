stored_binary = []


def conversion(x):
    global stored_binary
    stored_binary = []
    while x > 0:
        remainder = x % 2
        x = x // 2
        stored_binary.append(remainder)
        fixed_list =  stored_binary[::-1]

    return fixed_list

number_to_convert = int(input("write a numer to convert to binary: "))
print(conversion(number_to_convert))