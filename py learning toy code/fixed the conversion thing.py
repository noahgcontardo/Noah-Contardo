
#function because we love reusable code
def conversion(x):
    
#initialize locally
    stored_values = []
#set loop equal to number because once we store a binary value for every modulus calculuation we are done calculating the number
    while x > 0:
#modulus calculation to take our number and find the modulus of it (ie 30 modulus 9 is 3 because 3*9=27, 30-27=9)
#say the number we want to get is 15
        remainder = x % 2
#append result of the modulus calculation to a list, because it is modulus 2 the result will always be a 0 for even numbers and 1 for odd numbers as those are the only valid remainders
        stored_values.append(str(remainder))
#take the integer division of the number we inputted
        x = x // 2


    return "".join(reversed(stored_values))


number_to_convert = int(input("please provide an integer that you want converted to biary: "))
binary_result = conversion(number_to_convert)
print(binary_result)