#count number of vowels

vowel_count = 0

def scan_for_voewel(x):
    global vowel_count
    vowel_count = 0
    count_a = x.count('a')
    vowel_count += count_a
    count_e = x.count('e')
    vowel_count += count_e
    count_i = x.count('i')
    vowel_count += count_i
    count_o = x.count('o')
    vowel_count += count_o
    count_u = x.count('u')
    vowel_count += count_u
    print(vowel_count)

string_to_check = input("type some words and I'll tell you if they contain a vowel: ")
scan_for_voewel(string_to_check)