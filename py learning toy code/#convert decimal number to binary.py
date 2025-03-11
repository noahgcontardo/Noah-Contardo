#global array because ofc its a global array
stored_values = []
#function because we love reusable code
def conversion(x):
    while x > 0:

        remainder = x % 2
        stored_values.append(str(remainder))
        x = x // 2

    return "".join(reversed(stored_values))


number_to_convert = int(input("please provide an integer that you want converted to biary"))
binary_result = conversion(number_to_convert)
print(binary_result)