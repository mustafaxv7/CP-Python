'''                                              Nadour Moustafa                               '''


#1 One Variable Second Degree Equation Solver (6kyu)

from math import sqrt
def sec_deg_solver(a, b, c):
    if a == 0:# first case
        if b != 0 and c != 0 :
            return f'It is a first degree equation. Solution: {-float(c)/float(b)}'
        if b == 0 and c == 0 :
            return f'The equation is indeterminate'
        if b == 0 and c != 0 :
            return f'Impossible situation. Wrong entries'
        if b != 0 and c == 0 :
            return f'It is a first degree equation. Solution: 0.0'
    
    if a != 0:#second case
        delta = b**2 - (4*a*c)
        if delta < 0:
            return f'There are no real solutions'
        if delta == 0:
            return f'It has one double solution: {-b/(2*a)}'
        if delta > 0:
            root1 = (-b - sqrt(delta)) / (2*a)
            root2 = (-b + sqrt(delta)) / (2*a)
            if root1 == 0:
                return f"Two solutions: {-root1:.1f}, {root2:.10f}"
            if root2 == 0:
                return f"Two solutions: {-root2:.1f}, {root1:.10f}"
            return f"Two solutions: {round(min(root1, root2), 10):.10f}, {round(max(root1, root2), 10):.10f}"

#2 What century is it?(6kyu)
def extract_century(year):
    if int(year) % 100 == 0:
        century = int(year) // 100
    if int(year) % 100 > 0:
        century = (int(year) // 100) + 1
    return century
    
def what_century(year):
    century = extract_century(year)
    if century > 20:
        if century % 10 == 1:
            return f'{century}st'
        elif century % 10 == 2:
            return f'{century}nd'
        elif century % 10 == 3:
            return f'{century}rd'
        else:
            return f'{century}th'
    else:
        return f'{century}th'
            
        