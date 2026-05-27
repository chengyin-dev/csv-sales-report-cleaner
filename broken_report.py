import csv

file_path = "data/sales.csv"

total_sales = 0

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            quantity = int(row["quantity"])
            price = float(row["price"])

            if quantity <= 0 or price <= 0:
                print(f"Skipping invalid values: {row}")
                continue

            sale_total = quantity * price

            total_sales += sale_total

            print(f"{row['product']} => RM{sale_total}")

        except ValueError:
            print(f"Skipping invalid row: {row}")

print("-------------------")
print(f"TOTAL SALES: RM{total_sales}")