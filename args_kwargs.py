# 1 
def process_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:" kwargs)
process_data(1, 2, 3, name="Alice", age=25)
# Вывод:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}