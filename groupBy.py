import pandas as pd

data = {
    'Store': ['Lahore', 'Karachi', 'Lahore', 'Karachi', 'Islamabad'],
    'Sales': [500, 700, 300, 900, 400]
}
df = pd.DataFrame(data)

# Agar mujhe har sheher (Store) ki total sales chahiye:
city_sales = df.groupby('Store')['Sales'].sum()
print(city_sales)




import pandas as pd

data = {
    'Item': ['T-Shirt', 'Jeans', 'T-Shirt', 'Jeans', 'T-Shirt'],
    'Color': ['Blue', 'Black', 'Red', 'Blue', 'Black'],
    'Quantity': [5, 2, 3, 1, 4],
    'Earnings': [2500, 3000, 1500, 1500, 2000]
}
df = pd.DataFrame(data)

item_sales = df.groupby('Item')['Earnings'].sum()
print(item_sales)

color_quantity = df.groupby('Color')['Quantity'].sum()
print(color_quantity)


import pandas as pd
import numpy as np # Missing values (NaN) lagane ke liye numpy use hota hai

data = {
    'Naam': ['Asad', 'Sara', 'Fahad', 'Zoya'],
    'Umar': [25, np.nan, 22, 28], # Sara ki umar missing hai
    'City': ['Lahore', 'Karachi', None, 'Islamabad'] # Fahad ki city missing hai
}
df = pd.DataFrame(data)
print(df)

# Is line ko poora karein taake City ki missing value "Unknown" ban jaye
df['City'] = df['City'].fillna("Unknown") 
print(df)



import pandas as pd
import numpy as np

data = {
    'Item': ['Apple', 'Milk', 'Bread', 'Apple', 'Milk', 'Cookies'],
    'Category': ['Fruit', 'Dairy', 'Bakery', 'Fruit', 'Dairy', np.nan], # Cookies ki category missing hai
    'Price': [150, 120, 80, 160, 130, 200],
    'Quantity': [10, 5, 8, 12, 0, 6] # Milk ka stock 0 hai
}
df = pd.DataFrame(data)


df['Category'] = df['Category'].fillna("Snacks")
df['Total_Value'] = df['Price'] * df['Quantity']
df = df[df['Quantity'] > 0]
total_sales = df.groupby('Category')['Total_Value'].sum()
print(total_sales)
print(df)