def count_vowel(str):
    
    C = 0
    vow_set = {'a', 'e', 'i', 'o', 'u'}
    for char in str:
          if not char.isalpha():
               continue 
          elif char.lower() in vow_set:
              C += 1
          else:
              C -= 1
    return C
word_to_check = input('Please give me a word to count the difference of vowels and consonants: ')
print(count_vowel(word_to_check))