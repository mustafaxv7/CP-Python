'''                                       Nadour Moustafa        Fourth Set Of Problems             '''


#1 (a+b)^n(6kyu)




#2 Matrix Expansion(6kyu)




#3 Encrypt this!(6kyu)
def encrypt_this(text):
    if text == '':
        return ''
    text = text.split(' ')
    for word in range(len(text)):
        if len(text[word]) > 2:
            text[word] = str(ord(text[word][0])) + f'{text[word][-1]}{text[word][2:-1]}{text[word][1]}'
        elif len(text[word]) == 2:
            text[word] = str(ord(text[word][0])) + text[word][1:]
        else:
            text[word] = str(ord(text[word][0]))
    return ' '.join(word for word in text)


#4 Decipher this!(6kyu)
def decipher_this(text):
    if text == '':
        return ''
    text = text.split(' ')
    for word in range(len(text)):
        ascii_number = ''
        for letter in text[word]:
            if letter.isnumeric():
                ascii_number += str(letter)
                text[word] = text[word][1:]
        text[word] = (chr(int(ascii_number)) + f'{text[word][-1]}{text[word][1:-1]}{text[word][0]}') if len(text[word]) > 1 else chr(int(ascii_number)) + text[word]
    return ' '.join(word for word in text)

text = input('Enter a text to cipher: ')
print(decipher_this(text))



#5 Find The Parity Outlier(6kyu)
def is_odd(number):
    return False if number % 2 == 0 else True

def is_even(number):
    return True if number % 2 == 0 else False

def find_outlier(integers):
    outlier = integers[0]
    if (is_even(outlier) is not is_even(integers[1]) or (is_odd(outlier) is not is_odd(integers[1]))):
        return outlier
    for number in integers:
        if (is_even(outlier) is is_even(number)) or (is_odd(outlier) is is_odd(number)):
            continue
        else:
            outlier = number
            break
    return outlier


#Bonus: Extract the domain name from a URL(5kyu)
def domain_name(url):
    if 'www' in url:
        url = url.split('.')
        return url[1]
    if '//' in url:
        start = url.index('//')
        return url[start+2:url.index('.')]
    else:
        return url[:url.index('.')]