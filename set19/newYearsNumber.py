def isNewYearsNumber(n):
    if number < 2020:
        return 'NO'
    if n % 2020 == 0 or (n >= 2021 and (n - 2021) % 2020 == 0):
        return 'YES'
    return 'NO'

t = int(input())
numbers = list()
for times in range(t):
    number = int(input())
    numbers.append(number)

for number in numbers:
    print(isNewYearsNumber(number))