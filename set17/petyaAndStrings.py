s1 = input()
s2 = input()
if s1.lower() == s2.lower():
    print(0)
if s1.lower() < s2.lower():
    print(-1)
if s1.lower() > s2.lower():
    print(1)
