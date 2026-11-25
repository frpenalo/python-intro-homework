import csv

clean_data = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            rows_attempted = rows_attempted + 1

            # Check for extra columns
            if None in row:
                skipped_rows.append(
                    f"Row {row_number}: extra column detected — skipped"
                )
                continue

            try:
                name = row["name"]
                category = row["category"]
                amount = float(row["amount"])

                clean_row = {
                    "name": name,
                    "category": category,
                    "amount": amount
                }

                clean_data.append(clean_row)

            except ValueError:
                skipped_rows.append(
                    f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float"
                )

            except KeyError:
                skipped_rows.append(
                    f"Row {row_number}: KeyError — missing expected column"
                )

except FileNotFoundError:
    print("Error: messy_data.csv was not found.")

else:
    print("=== CSV Report ===")
    print(f"Rows attempted:  {rows_attempted}")
    print(f"Rows parsed:      {len(clean_data)}")
    print(f"Rows skipped:     {len(skipped_rows)}")

    print("\nSkipped rows:")

    for skipped in skipped_rows:
        print(f"  {skipped}")

    print("\nClean data:")

    for row in clean_data:
        print(
            f'  {row["name"]} | {row["category"]} | ${row["amount"]:.2f}'
        )