import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Company sales analysis
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

sales = []

print("********* COMPANY SALES ANALYSIS********")

print("Enter monthly sales in $10,000:\n")

# Taking input
for month in months:
    value = float(input(f"{month} : "))
    sales.append(value)

# Convert list to NumPy array
sales = np.array(sales)

# Analysis of sales 

total_sales = np.sum(sales)
average_sales = np.mean(sales)
maximum_sales = np.max(sales)
minimum_sales = np.min(sales)

best_month = months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]


above_average = months[sales > average_sales]
below_average = months[sales < average_sales]

#TOP 3 MONTH

top_3_index = np.argsort(sales)[-3:][::-1]
top_3_months = months[top_3_index]
top_3_sales = sales[top_3_index]

# growth check
growth = np.diff(sales)

growth_month = months[1:][np.argmax(growth)]
decline_month = months[1:][np.argmin(growth)]

#pandas implement
df = pd.DataFrame({
    "Month": months,
    "Sales ($10,000)": sales
})

# Add performance column
df["Performance"] = np.where(
    df["Sales ($10,000)"] >= average_sales,
    "Good",
    "Needs Improvement"
)

#Result display


print("*********SALES ANALYSIS REPORT********")


print(f"Total Yearly Sales       : ${total_sales:.2f} × 10,000")
print(f"Average Monthly Sales    : ${average_sales:.2f} × 10,000")
print(f"Maximum Monthly Sales    : ${maximum_sales:.2f} × 10,000")
print(f"Minimum Monthly Sales    : ${minimum_sales:.2f} × 10,000")

print(f"\nBest Month               : {best_month}")
print(f"Worst Month              : {worst_month}")

print("\nAbove Average Months:")
print(above_average)

print("\nBelow Average Months:")
print(below_average)

print("\nTop 3 Sales Months:")

for i in range(3):
    print(
        f"{i+1}. {top_3_months[i]} "
        f"→ ${top_3_sales[i]:.2f} × 10,000"
    )

print(f"\nHighest Growth Month     : {growth_month}")
print(f"Highest Decline Month    : {decline_month}")

#pd

print("*********MONTHLY SALES ANALYSIS REPORT********")

print(df.to_string(index=False))

#data saved with csv

df.to_csv("company_sales.csv", index=False)

print("\nData saved successfully to company_sales.csv")

#matploty

plt.figure(figsize=(10, 5))

plt.bar(months, sales)

plt.title("Company Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($10,000)")

plt.axhline(
    average_sales,
    linestyle="--",
    label=f"Average = {average_sales:.2f}"
)

plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.show()

#sales follow

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($10,000)")

plt.grid(True)

plt.show()