data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [28, 32, 25],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

# Find the maximum length for each column
column_widths = {}
for key, values in data.items():
    max_value_length = max(len(str(value)) for value in values)
    column_widths[key] = max(len(key), max_value_length)

# Print header
header = ''
for key, width in column_widths.items():
    header += f"{key:{width}s} | "
print(header.rstrip())

# Print separator
separator = ''
for width in column_widths.values():
    separator += '-' * width + '-+-'
print(separator.rstrip())

# Print rows
num_rows = len(data[list(data.keys())[0]])
for i in range(num_rows):
    row = ''
    for key, width in column_widths.items():
        row += f"{str(data[key][i]):{width}s} | "
    print(row.rstrip())
