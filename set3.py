'''                                      Nadour Moustafa                                      '''
# Third  Set Of  Problems

#1 Leap Years(7kuy)
def is_leap_year(year):
    isleap = False
    if year % 4 == 0:
        isleap = True
        if year % 100 == 0:
            isleap = False
            if year % 400 == 0:
                isleap = True
    return isleap


#2 Bit Counting(6kuy)
def countBits(n):
    return bin(n).count('1')
    

#4 Persistent Bugger.(6kuy)
def persistence(n):
    counter = 0
    while len(str(n)) > 1:
        mul = 1
        for i in str(n):
            mul *= int(i)
        counter += 1
        n = mul
    return counter


#5 Matrix Transpose(6kuy)
def transpose(matrix):
    column = 0
    matrix_transposer = []
    while column < len(matrix[0]):
        sub_ligne = []
        for ligne in range(len(matrix)):
            sub_ligne.append(matrix[ligne][column])
        matrix_transposer.append(sub_ligne)
        column += 1
    return matrix_transposer



#Bonus: The Hashtag Generator(5kuy)
def generate_hashtag(s):
    if s == '':
        return False
    result = '#'+''.join(word.title() for word in s.split(' '))
    if len(result) > 140:
        return False
    else: return result

'''                                Good Luck Guys'''