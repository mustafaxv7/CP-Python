def shift_to_be_deffrent(stones,stonesColor):
    shifts = 0
    for color in range(len(stonesColor)-1):
        if stonesColor[color] == stonesColor[color+1]:
            shifts +=1
    return shifts
        
n = int(input())
stonesColor = input()
print(shift_to_be_deffrent(n,stonesColor))