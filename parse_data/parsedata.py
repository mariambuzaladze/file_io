import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    data = list(reader)

headers = ["Last", "First", "Salary"]

col_widths = [max(len(row[i]) for row in data + [headers]) for i in range(len(headers))]

print(f"{headers[0]:<{col_widths[0]}} | {headers[1]:<{col_widths[1]}} | {headers[2]:<{col_widths[2]}}")
print("-" * (sum(col_widths) + len(headers) * 3 - 2))

for row in data:
    print(f"{row[0]:<{col_widths[0]}} | {row[1]:<{col_widths[1]}} | {row[2]:<{col_widths[2]}}")
