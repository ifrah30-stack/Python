import csv

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Alice"])
print("Employee record saved.")
