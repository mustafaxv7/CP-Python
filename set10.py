'''                                              Nadour Moustafa                               '''

#1 Highest Scoring Word(6kyu)
import string
def score_of_word(word):
    score = 0
    for letter in word:
        score += (string.ascii_lowercase.index(letter) + 1)
    return score
def high(str):
    str = str.split(' ')
    highest_score = score_of_word(str[0])
    highest_score_word = str[0]
    for word in str:
        if highest_score < score_of_word(word):
            highest_score = score_of_word(word)
            highest_score_word = word
    return highest_score_word

print(score_of_word('abad'))

#2 Basic Encryption(6kyu)
def encrypt(text, rule):
    rule %= 256
    encrypted_text = ''
    for letter in text:
        encrypted_text += chr((ord(letter) + rule) % 256)
    return encrypted_text