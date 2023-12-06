'''                                                Nadour Moustafa                                  '''
#2 Valid braces
def valid_braces(string):
    opened_braces = []
    for brace in string:
        if brace == '(' or brace == '[' or brace == '{':
            opened_braces.append(brace)
        if brace == ')':
            if opened_braces == []:
                return False
            if opened_braces[-1] == '(':
                opened_braces.pop()
            else:
                return False
        if brace == ']':
            if opened_braces == []:
                return False
            if opened_braces[-1] == '[':
                opened_braces.pop()
            else:
                return False
        if brace == '}':
            if opened_braces == []:
                return False
            if opened_braces[-1] == '{':
                opened_braces.pop()
            else:
                return False
    if opened_braces == []:
        return True
    else: return False


#Bonus: Is a number prime?(6kyu)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True