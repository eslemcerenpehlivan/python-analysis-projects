import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

np.random.seed(42)

products = [
    "Milk", "Bread", "Rice", "Apple",
    "Chicken", "Juice", "Cheese", "Banana"
]

categories = [
    "Dairy", "Bakery", "Grocery", "Fruit",
    "Meat", "Beverage", "Dairy", "Fruit"
]

sales = np.random.randint(80, 201, size=len(products))

df = pd.DataFrame({
    "Product": products,
    "Category": categories,
    "Sales": sales
})

print(f"Total Sales      : {df['Sales'].sum()}")
print(f"Average Sales    : {df['Sales'].mean():.2f}")
print(f"Highest Sale     : {df['Sales'].max()}")
print(f"Lowest Sale      : {df['Sales'].min()}")

best_product = df.loc[df["Sales"].idxmax(), "Product"]
worst_product = df.loc[df["Sales"].idxmin(), "Product"]

print(f"Best Selling Product  : {best_product}")
print(f"Lowest Selling Product: {worst_product}")

sorted_df = df.sort_values(by="Sales", ascending=False)

print(sorted_df)

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

print(category_sales)

plt.figure(figsize=(10,5))

plt.bar(sorted_df["Product"], sorted_df["Sales"])

plt.title("Product Sales (Matplotlib)")
plt.xlabel("Products")
plt.ylabel("Sales")

for i, value in enumerate(df["Sales"]):
    plt.text(i, value + 2, str(value), ha="center")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))

sns.barplot(
    data=category_sales,
    x="Category",
    y="Sales"
)

plt.title("Category Sales (Seaborn)")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()