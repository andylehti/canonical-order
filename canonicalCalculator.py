def normEx(e):
    return e.replace(' ', '').replace('**', '^').replace('^', '**')

def nestEx(e):
    s = []
    for i, c in enumerate(e):
        if c == '(':
            s.append(i)
        elif c == ')':
            return s.pop(), i
    return -1, -1

def simpEx(e):
    e = normEx(e)
    x = [e]
    while '(' in e:
        a, b = nestEx(e)
        if a == -1 or b == -1:
            break
        r = str(eval(e[a + 1:b]))
        e = e[:a] + r + e[b + 1:]
        x.append(e)
    x.append(f"= {eval(e)}")
    return x

def calcEx(e):
    x = simpEx(e)
    for s in x:
        print(s)
    return

input_expression = "(1 + 2) * (3 + 4 / 5 - (6 * (7 / 8 + (9 - (1 + 2) / 3)^2 + 4 - (5 * (6 / 7) - 8 + (-9 * (-1 + 2)^5 - 3 / 4 + (5 - 6 * (7 / 8 + (9 - (1 + 2) / 3) + (4 - 5 * (6 / 7) - 8 + (9 * (1 + 2) - 3 / (4 + 5 - 6 * (7 / 8 + (9 - (1 + 2) / 3) + 4 - (5 * (6 / 7) - 8 + 9 * (1 + 2) - 3 / 4)))))))))))^2)^2"
calcEx(input_expression)
