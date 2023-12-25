'''                                    Nadour Moustafa                                   '''

#2 Is Integer Array?(6kyu)
def is_int_array(arr):
    if arr is None or arr == '':
        return False
    try:
        arr = iter(arr)
    except:
        return False
    if isinstance(arr,dict):
        return False
    
    new_arr = [(isinstance(i,int) or (isinstance(i,float)) and i.is_integer()) for i in arr]
    return all(new_arr)