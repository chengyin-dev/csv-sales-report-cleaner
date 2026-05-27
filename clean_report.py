import csv
from pathlib import Path

DATA_FILE = Path("data") / "sales.csv"


def read_sales_report(file_path):
    total_sales = 0
    valid_rows = 0
    skipped_rows = 0

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                quantity = int(row["quantity"])
                price = float(row["price"])

                if quantity <= 0 or price <= 0:
                    skipped_rows += 1
                    print(f"Skipped invalid values: {row}")
                    continue

                sale_total = quantity * price
                total_sales += sale_total
                valid_rows += 1

                print(f"{row['product']} => RM{sale_total:.2f}")

            except ValueError:
                skipped_rows += 1
                print(f"Skipped invalid row: {row}")

    print("-------------------")
    print(f"Valid rows: {valid_rows}")
    print(f"Skipped rows: {skipped_rows}")
    print(f"Total sales: RM{total_sales:.2f}")


read_sales_report(DATA_FILE)