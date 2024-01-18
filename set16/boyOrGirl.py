username = str(input())
duplicated_letters = []
seen_letters = set()
for letter in username.lower():
    if letter in seen_letters:
        duplicated_letters.append(letter)
    else:
        seen_letters.add(letter)
numberOfdistenct = len(username.lower())- len(duplicated_letters)
if numberOfdistenct % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')