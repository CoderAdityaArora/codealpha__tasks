import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = []
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "Stock": stock_name,
        "Price": price,
        "Quantity": quantity,
        "Investment": investment
    })

    add_more = input("Do you want to add another stock? (yes/no): ").lower()
    if add_more != "yes":
        break

print("\nPortfolio Summary")
print("-" * 40)

for item in portfolio:
    print(
        f"{item['Stock']} | "
        f"Price: ${item['Price']} | "
        f"Quantity: {item['Quantity']} | "
        f"Value: ${item['Investment']}"
    )

print("-" * 40)
print(f"Total Investment Value: ${total_investment}")

save = input("\nDo you want to save the result? (txt/csv/no): ").lower()

if save == "txt":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-" * 40 + "\n")

        for item in portfolio:
            file.write(
                f"{item['Stock']} | "
                f"Price: ${item['Price']} | "
                f"Quantity: {item['Quantity']} | "
                f"Value: ${item['Investment']}\n"
            )

        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Result saved as portfolio_summary.txt")

elif save == "csv":
    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Price", "Quantity", "Investment"])

        for item in portfolio:
            writer.writerow([
                item["Stock"],
                item["Price"],
                item["Quantity"],
                item["Investment"]
            ])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print("Result saved as portfolio_summary.csv")

else:
    print("Result not saved.")