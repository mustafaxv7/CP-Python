'''                                       Nadour Moustafa                             '''

#2 One down(6kyu)

def one_down(txt):
    decoded_txt = ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if type(txt) is not str:
        return 'Input is not a string'
    if txt == '':
        return ''
    else:
        for letter in txt:
            if letter == ' ':
                decoded_txt += ' '
            else:
                if letter in alphabet:
                    if letter.isupper():
                        decoded_txt += alphabet[alphabet.index(letter)-1].upper()
                    if letter.islower():
                        decoded_txt += alphabet[alphabet.index(letter)-1].lower()
                else:
                    decoded_txt += letter
    return decoded_txt

#-----------------------------------------------------------------------------------

