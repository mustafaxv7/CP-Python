
'''                       Nadour Moustafa work assignment              '''

#Dismevowel Trolls (7 kyu)
def disemvowel(string):
    for letter in string:
        if letter == 'a' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'e' or letter == 'A' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'E':
            string = string.replace(letter,'')
    return string


#String ends with? (7kyu)
def solution(text, ending):
    return text[len(text)-len(ending):]  == ending


#Square Every Digit(7kyu)
def square_digits(num):
    squared_num = ''
    for i in str(num):
        squared_num += str(int(i) * int(i))
    return int(squared_num)

    
#Highest and Lowest(7kyu)
def high_and_low(numbers):
    numbers = [int(number) for number in numbers.split(' ')]
    return f'{max(numbers)} {min(numbers)}'


#Get the Middle Character(7kyu)
def get_middle(s):
    if len(s) % 2 != 0:
        return s[int(len(s)/2)]
    else:
        return s[int(len(s)/2)-1] + s[int(len(s)/2)]
    

#List Filtering(7kyu)
def filter_list(l):
    'return a new list with the strings filtered out'
    return [i  for i in l if type(i) == int]


#You're a square!(7kyu)
from math import sqrt
def is_square(n):    
    if n < 0:
        return False
    else:
        if sqrt(n) % 1 == 0:
            return True
        else: return False


#Exes and Ohs(7kyu)
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


#Jaden Casing Strings(7kyu)
def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split(' ')])


#Complementary DNA(7kyu)
def DNA_strand(dna):
    complementary_dna_side = ''
    for asout_unit in dna.upper():
        if asout_unit == 'A':
            complementary_dna_side += 'T'
        elif asout_unit == 'T':
            complementary_dna_side += 'A'
        elif asout_unit == 'C':
            complementary_dna_side += 'G'
        elif asout_unit == 'G':
            complementary_dna_side += 'C'
        else:
            print('Not Human DNA')
    return complementary_dna_side


#Bonus: Stop gninnipS My sdroW!(6kyu)
def spin_words(sentence):
    sentence = sentence.split(' ')
    sentence = [word[::-1] if len(word) >= 5 else word for word in sentence]
    return ' '.join(sentence)



'''                           Good Luck For Others                               '''