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

# Determine the maximum key length for formatting
max_key_length = max(len(key) for key in data[0].keys())

# Print header
header = ' ' * max_key_length + ' | '
for i, width in enumerate(value_widths):
    header += f"{data[i]['Product']:{width}s} | "
print(header.rstrip())

# Print separator
separator = '-' * max_key_length + '-+-'
for width in value_widths:
    separator += '-' * width + '-+-'
print(separator.rstrip())

# Print rows
keys = list(data[0].keys())
for key in keys[1:]:
    row = ''
    for i, width in enumerate(value_widths):
        row += f"{str(data[i][key]):{width}s} | "
    print(f"{key:{max_key_length}s} | {row.rstrip()}")

    

### Output looks like this
#          | Product 1 | Product 2
#----------+-----------+----------
#Price     | 120.5     | 199.99
#Quantity  | 15        | 8
#In Stock  | True      | False

