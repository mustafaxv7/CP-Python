def proved_solution(opinions):
    if opinions.count(1) > 1 :
        return 1
        
n = int(input())
counter = 0
for i in range(n):
    opinions = list(map(int,input().split()))
    if proved_solution(opinions) == 1:
        counter += 1
print(counter)
