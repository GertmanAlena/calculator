import test

x = 0
y = 0
z = 0

def num(a, c, b):
    global x
    global z
    global y
    x = a
    z = c
    y = b

def operator():
    if z == '+':
        return x + y
    if z == '-':
        return x - y
    if z == '*':
        return x * y
    if z == '/':
        return test.div(x, z, y)
    