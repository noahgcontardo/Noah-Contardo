word_entered = str(input('please provide a word to dot-ify: '))

dotified = []

for x in range(len(word_entered)):
    if x == len(word_entered) -1:
        dotified.append(word_entered[x])
    elif word_entered[x].isalnum() == True:
        dotified.append(word_entered[x] + ".")    
    else:
        continue
    
            
fixed_bullshit = "".join(dotified)
print(fixed_bullshit)