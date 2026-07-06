# Yeh data diya hai tumhe — khud analysis karo
import pandas as pd
cricket_data = {
    "player": ["Babar", "Rizwan", "Fakhar", "Imam", "Shadab"],
    "matches": [45, 42, 38, 35, 40],
    "runs": [2100, 1890, 1650, 1420, 890],
    "wickets": [0, 0, 0, 0, 45],
    "country": ["Pakistan"] * 5
}

df_cricket = pd.DataFrame(cricket_data)

# Tumhe yeh karna hai:
# 1. df_cricket.head() se data dekho
# 2. Average runs calculate karo
# 3. Sirf 1500+ runs wale players filter karo
# 4. "runs_per_match" naam ka naya column banao
# 5. Ek bar chart banao players vs runs ka

print(df_cricket.head())
df_average = df_cricket['runs'].mean()
df_maximum = df_cricket[df_cricket["runs"] > 1500]
print("Average runs:", df_average)
print("Players with more than 1500 runs:")
print(df_maximum)

df_cricket["Runs Per Match"] = df_cricket["runs"] / df_cricket["matches"]
print("\nData with Runs Per Match.")
print(df_cricket)

import matplotlib.pyplot as plt

plt.bar(df_cricket["players"], df_cricket["runs"])
plt.xlabel("Players")
plt.ylabel("Runs")
plt.title("Players vs Runs")
plt.show()


