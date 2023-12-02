'''                                    Nadour Moustafa    Second Set                      '''
#Sum of two lowest positive integers(7kyu)
def sum_two_smallest_numbers(numbers):
    lowest_number = min(numbers)
    numbers.remove(lowest_number)
    return lowest_number + min(numbers)
 

#Printer Errors(7kyu)
def printer_error(s):
    errors = 0
    for color in s.lower():
        if color > 'm':
            errors += 1
    return f'{errors}/{len(s)}'


# Regex validate PIN code(7kyu)
def validate_pin(pin):
    return pin.isnumeric() and (len(pin) == 4 or len(pin) == 6)


#Binary Addition(7kyu)
def add_binary(a,b):
    somme = a + b
    binary = ''
    while True:
        binary += str(somme % 2)
        somme = somme // 2
        if somme == 0:
            break
    return binary[::-1]


#Is this a triangle?(7kyu)
def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

#The Coupon Code(7kyu)
"""i will try on it later on """

#Sorted? yes? no? how?(7kyu)
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr,reverse = True):
        return 'yes, descending'
    else:
        return 'no'


#Fizz Buzz(7kyu)
def fizzbuzz(n):
    arr = []
    for number in range(1,n+1):
        if number % 3 == 0 and number % 5 == 0:
            arr.append('FizzBuzz')
        elif number % 3 == 0:
            arr.append('Fizz')
        elif number % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(number)
    return arr


#Convert string to camel case(6kyu)
def to_camel_case(text):
    text = text.replace('-','_')
    if '_' in text:
        text = text.split('_')
        return text[0] + ''.join([word.capitalize() for word in text[1:]])
    else:
        return ''


#Tribonacci Sequence(6kyu)
def tribonacci(signature, n):
    if n == 0:
        return []
    while len(signature) != n:
        signature.append(sum(signature[-3:])) 
    return signature