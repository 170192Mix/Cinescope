
def func1(x): return x + 1
def func2(x): return x * 2
def func3(x): return x**2

result = func1(func2(func3(2))) # Тут несколько вызовов

print(result)