def rearrangeEq(equation):
    equation = equation.split('+')
    equation.sort()
    return '+'.join(equation)
    

equation = input()
print(rearrangeEq(equation))
