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

# Transpose the data
headers = list(data[0].keys())
transposed_data = list(zip(*[d.values() for d in data]))

# Create the HTML table
html_table = '<table border="1">\n'

# Add table rows with headers and data
for i, header in enumerate(headers):
    html_table += '  <tr>\n'
    html_table += f'    <th>{header}</th>\n'
    for value in transposed_data[i]:
        html_table += f'    <td>{value}</td>\n'
    html_table += '  </tr>\n'

html_table += '</table>'

print(html_table)

"""
Final output table:

Product	Product 1	Product 2
Price	120.5	199.99
Quantity	15	8
In Stock	True	False
"""
