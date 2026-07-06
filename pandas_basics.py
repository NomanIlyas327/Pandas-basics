# pandas basics
# Data ko dictionary me likha
import pandas as pd
data = {
    'Naam': ['Ali', 'Ayesha', 'Zain', 'Sara'],
    'Umar': [22, 21, 23, 22],
    'Score': [85, 92, 78, 95]
}

# Is data ko DataFrame me convert kiya
df = pd.DataFrame(data)

# Data ko dekhne ke liye
print(df)
print("\nDataFrame ke columns:")
print(df.columns)
print("\nDataFrame ke shape:")
print(df.shape)
print("\nDataFrame ke head:")
print(df.head())
print("\nDataFrame ke tail:")
print(df.tail())
print("\nDataFrame ke summary statistics:")
print(df.describe())
print("\nDataFrame ke data types:")
print(df.dtypes)
print("\nDataFrame ke index:")
print(df.index)
print("\nDataFrame ke values:")
print(df.values)
print("\nDataFrame ke info:")
print(df.info())
print("\nDataFrame ke specific column (Naam):")
print(df['Naam'])




import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Charger'],
    'Price': [1200, 800, 350, 150, 30],
    'Stock': [15, 25, 0, 50, 0]
}
df = pd.DataFrame(data)
# df = df[df['Price']>500]
# print(df)
out_of_stock = df[df['Stock'] == 0]

print(out_of_stock)
df['total_value'] = df['Price'] * df['Stock']
print(df)