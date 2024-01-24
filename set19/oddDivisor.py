def hasOddDivisor(n):
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0 and i % 2 != 0:
            return "YES"
    return "NO"

t = int(input())
numbers = []
for _ in range(t):
    n = int(input())
    numbers.append(n)

for number in numbers:
    print(hasOddDivisor(number))

