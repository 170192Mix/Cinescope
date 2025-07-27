def a(x): print("a"); return x + 1
def b(x): print("b"); return x * 2
def c(x): print("c"); return x ** 2

result = a(b(c(2))) # Поставьте тут точку останова
print(result)