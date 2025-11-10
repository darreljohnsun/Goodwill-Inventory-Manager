import pandas as pd
import sqlite3
from jinja2 import Template

# Step 1: Load CSV
df = pd.read_csv('products.csv')

# Step 2: Clean / Validate Data
df = df.drop_duplicates(subset='product_id')
df = df.dropna()
df = df[df['price'] >= 0]
df = df[df['stock'] >= 0]

print("Cleaned Data:")
print(df)

# Step 3: Save to SQLite Database
conn = sqlite3.connect('inventory.db')
df.to_sql('products', conn, if_exists='replace', index=False)
print("Data saved to inventory.db")

# Step 4: Generate HTML page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Inventory</title>
</head>
<body>
    <h1>Product Inventory</h1>
    <ul>
    {% for product in products %}
        <li>
            <img src="{{ product.image_url }}" width="100" height="100">
            <strong>{{ product.name }}</strong> - {{ product.category }} - ${{ product.price }} - Stock: {{ product.stock }}
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

template = Template(html_template)
html_content = template.render(products=df.to_dict(orient='records'))

with open('inventory.html', 'w') as f:
    f.write(html_content)

print("HTML inventory page generated: inventory.html")

conn.close()
