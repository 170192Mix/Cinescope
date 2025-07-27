def process_data(data):
    processed_data = transform_data(data)
    result = calculate_result(processed_data)
    return result

def transform_data(data):
    return [x * 2 for x in data]

def calculate_result(data):
    return sum(data)

data = [1, 2, 3]
final_result = process_data(data)
print(final_result)