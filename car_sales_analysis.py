import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(42)


brands = ["Toyota", "BMW", "Mercedes", "Audi", "Tesla", "Ford"]

sales = np.random.randint(80, 201, size=len(brands))

df = pd.DataFrame({
    "Brand": brands,
    "Cars Sold": sales
})

df = df.sort_values(by="Cars Sold", ascending=False)

print(f"Total Cars Sold : {df['Cars Sold'].sum()}")
print(f"Average Sales   : {df['Cars Sold'].mean():.2f}")
print(f"Highest Sales   : {df['Cars Sold'].max()}")
print(f"Lowest Sales    : {df['Cars Sold'].min()}")

best_brand = df.loc[df["Cars Sold"].idxmax(), "Brand"]
worst_brand = df.loc[df["Cars Sold"].idxmin(), "Brand"]

print(f"Best Selling Brand  : {best_brand}")
print(f"Lowest Selling Brand: {worst_brand}")

plt.figure(figsize=(8,5))
plt.bar(df["Brand"], df["Cars Sold"])

plt.title("Car Sales by Brand (Matplotlib)")
plt.xlabel("Brand")
plt.ylabel("Cars Sold")

for i, value in enumerate(df["Cars Sold"]):
    plt.text(i, value + 2, str(value), ha="center")

plt.show()

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Brand",
    y="Cars Sold"
)

plt.title("Car Sales by Brand (Seaborn)")
plt.xlabel("Brand")
plt.ylabel("Cars Sold")

plt.show()
