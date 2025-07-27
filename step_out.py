def inner(a, b):
    c = a + b
    d = c * 2 # Поставьте тут точку останова
    return d

def outer(x):
    y = 10
    z = inner(x, y)
    return z

result = outer(5)
print(result)