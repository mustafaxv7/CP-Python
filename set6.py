'''                                     Nadour Moustafa            Sexth  Set Of Problems (Codewars)                                       '''

#1 Duplicate Encoder (6kyu)
def duplicate_encode(word):
    encoded_message = ''
    word = word.lower()
    for letter in word:
        print(letter)
        if word.count(letter) == 1:
            print(letter)
            encoded_message += '('
        else:
            encoded_message += ')'
    return encoded_message




#3 Detect Pangram (6kyu)
def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    for letter in s.lower():
        if letter.isalpha() and letter in alphabet:
            alphabet.remove(letter)
            if not alphabet:
                return True
    return False
    





#4 Crack the PIN(6kyu)
from hashlib import md5
def crack(hash):
    pin = '00000'
    step = 1
    while True:
        if md5(pin.encode()).hexdigest() == hash:
            break
        pin = f'{(len(pin)-len(str(step)))*str(0)}{str(step)}'
        step += 1
    return pin
    
          
    
     
           
        
    
