'''                                       Nadour Moustafa                                   '''


#1 Write Number in Expanded Form(6kyu)

def expanded_form(num):
    pos = 1
    expanded_form = list()
    while num != 0:
        unit = (num % 10) * pos
        pos *= 10
        if unit != 0:
            expanded_form.insert(0,str(unit))
        num = num // 10
    return ' + '.join(expanded_form)

#-----------------------------------------------------------------------------

#2 Help the bookseller !(6kyu)

def stock_list(list_of_art, list_of_cat):
    if list_of_art == [] or list_of_cat == []:
        return ''
    result = []
    list_of_art.sort()
    for category in list_of_cat:
        total_quantity = 0
        for book in list_of_art:
            if book.startswith(category):
                quantity = int(book.split()[1])
                total_quantity += quantity
        result.append(f'({category} : {total_quantity})')
    return ' - '.join(result)

'''                                  Good Luck                                           '''