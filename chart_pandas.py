# Pehle ek CSV file banate hain (Pakistan shop sales data)
import pandas as pd
import matplotlib.pyplot as plt

shop_data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "product": ["Shirt", "Pants", "Shirt", "Shoes", "Pants", "Shirt", "Shoes", "Pants"],
    "city": ["Lahore", "Karachi", "Islamabad", "Lahore", "Karachi", "Lahore", "Islamabad", "Karachi"],
    "price": [1500, 2500, 1500, 3500, 2500, 1500, 3500, 2500],
    "quantity": [2, 1, 3, 1, 2, 1, 2, 3],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Apr"]
}

df_shop = pd.DataFrame(shop_data)

# CSV save karo
df_shop.to_csv('pakistan_shop_sales.csv', index=False)
print("CSV file ban gayi!")

# Ab wapas load karo (real duniya mein yahi karte hain)
df_loaded = pd.read_csv('pakistan_shop_sales.csv')
print("\nCSV load ho gayi:")
print(df_loaded)

total_revenue = df_loaded['price'] * df_loaded['quantity']
df_loaded['total_revenue'] = total_revenue

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: City revenue bar chart
city_rev = df_loaded.groupby("city")["total_revenue"].sum()
axes[0].bar(city_rev.index, city_rev.values, color=["#378ADD", "#1D9E75", "#EF9F27"])
axes[0].set_title("Revenue by City")
axes[0].set_xlabel("City")
axes[0].set_ylabel("Revenue (PKR)")
for i, v in enumerate(city_rev.values):
    axes[0].text(i, v + 100, str(v), ha='center', fontweight='bold')

# Chart 2: Product sales pie chart
product_rev = df_loaded.groupby("product")["total_revenue"].sum()
axes[1].pie(product_rev.values, labels=product_rev.index,
            autopct='%1.1f%%', colors=["#378ADD", "#1D9E75", "#EF9F27"])
axes[1].set_title("Revenue by Product")

plt.suptitle("Pakistan Shop Sales Analysis", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('day2_sales_charts.png', dpi=150)
plt.show()
print("Charts ready!")