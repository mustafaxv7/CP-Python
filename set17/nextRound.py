n , k = map(int,input().split())
goNextRound = 0
scores = list(map(int,input().split()))
kthScore = scores[k-1]
for score in scores:
    if score >= kthScore  and score > 0:
        goNextRound += 1
print(goNextRound)
