#global arrays to store values for EEA
quotient = []
remainder = []
#initialization of Bezout's Identity numbers for EEA
s_value = [1,0]
t_value = [0,1]

inputty_1 = int(input("give a prime number: "))
inputty_2 = int(input('give a different prime number: '))

#please interpret
def getEcclidean():

    remainder.append(inputty_1)
    remainder.append(inputty_2)

    i = 1

    while remainder[i] != 1:
#we need the remainder to be equal to 1 because the inputs should ONLY be coprime
#this means a remainder of 1 is guarunteed

#calculate current remainder 'r' based on first remainder entered modulus second remainder
        r = remainder[i-2] % remainder[i-1]
#calculate quotient based on integer division of remainders
        q = (remainder[i-2] - remainder[i]) // remainder[i-1]
#add to array
        quotient.append(q)
        remainder.append(r)
#calculate inverse modulus to establish secrets we can use to reverse a mathematically related key pair
        s = s_value[i-2] - quotient[i-1] * s_value[i-1]
        t = t_value[i-2] - quotient[i-1] * t_value[i-1]
#add inverse modulus values to the arrays
        s_value.append(s)
        t_value.append(t)
#increase iteration value
        i += 1