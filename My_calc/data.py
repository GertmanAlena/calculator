
x = 0
y = 0
z = 0

def num(a, b, c):
    global x
    global y
    global z
    x = a
    y = b
    z = c

def operator():
    if z == '+':
        return x + y
    if z == '-':
        return x - y
    if z == '*':
        return x * y
    if z == '/':
        return x / y
