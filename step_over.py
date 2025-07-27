
def inner_function(x):
    return x * 2

def outer_function(a):
    b = inner_function(a + 1)  # Step Over здесь
    c = b * 3                # После Step Over выполнение будет здесь
    return c

result = outer_function(5)
print(result)