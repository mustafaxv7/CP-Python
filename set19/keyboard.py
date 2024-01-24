def expresion(text,side):
    keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    right_expresion = ''
    if side == 'R':
        for letter in text:
            right_expresion += keyboard[keyboard.index(letter)-1]
    if side == 'L':
        for letter in text:
            right_expresion += keyboard[keyboard.index(letter)+1]
    return right_expresion
side = input()
text = input()
print(expresion(text,side))
