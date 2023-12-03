'''                                             Nadour Moustafa                 Seventh Set Of Problems'''

#1 Unique In Order(6kyu)

def unique_in_order(sequence):
    if not sequence:
        return []
    unique_sequence = [sequence[0]]
    for letter in sequence[1:]:
        if letter != unique_sequence[-1]:
            unique_sequence.append(letter)
    return unique_sequence

#2 Find the unique number(6kyu)

def find_uniq(arr):
    outsider = arr[0]
    n = 1
    if outsider is not arr[n] and arr[n] is arr[n+1]:#first element case
        return outsider
    for n in arr[1:]:
        if outsider is n:
            continue
        else:
            return n