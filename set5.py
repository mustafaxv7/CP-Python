'''                                 Nadour Moustafa      Fifth Set                  '''
#1 Equal Sides Of An Array(6kyu)
def find_even_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1:])
        if left_sum == right_sum:
            return i
    return -1


#2 Playing with digits(6kyu)
def dig_pow(n, p):
    somme = 0
    for digit in str(n):
        somme += int(digit)**p
        p+=1
        if somme == (n * int(somme/n)):
            return int(somme/n)
    return -1


#3 Who likes it?(6kyu)
def likes(names):
    if names == []:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    

#4 Your order, please(6kyu)
def getIndex(word):
    for letter in word:
        if letter.isnumeric():
            return int(letter)
    
def order(sentence):
    if not sentence:
        return ''
    sentence = sentence.split(' ')
    ordered_list = sorted(sentence,key = lambda word: getIndex(word))
    return ' '.join(ordered_list)


    
#5 uniq (UNIX style)(6kyu)
def uniq(seq): 
    if not seq:
        return []
    uniq_seq = [seq[0]]
    for element in seq[1:]:
        if element != uniq_seq[-1]:
            uniq_seq.append(element)
    return uniq_seq

#                                  Good Luck guys i hope it was easy for you