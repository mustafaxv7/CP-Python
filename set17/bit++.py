n = int(input())
x = 0
for i in range(n):
    statement = input()
    if '+' in statement:
        x += 1
    else: x -= 1
print(x)