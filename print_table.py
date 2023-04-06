data = [
    {
        'Product': 'Product 1',
        'Price': 120.50,
        'Quantity': 15,
        'In Stock': True
    },
    {
        'Product': 'Product 2',
        'Price': 199.99,
        'Quantity': 8,
        'In Stock': False
    }
]

# Find the maximum length for each value
value_widths = []
for product in data:
    max_value_length = max(len(str(value)) for value in product.values())
    value_widths.append(max_value_length)

# Print header
header = ''
for i, width in enumerate(value_widths):
    header += f"{data[i]['Product']:{width}s} | "
print(header.rstrip())

# Print separator
separator = ''
for width in value_widths:
    separator += '-' * width + '-+-'
print(separator.rstrip())

# Print rows
keys = list(data[0].keys())
for key in keys[1:]:
    row = ''
    for i, width in enumerate(value_widths):
        row += f"{str(data[i][key]):{width}s} | "
    print(f"{key} | {row.rstrip()}")
