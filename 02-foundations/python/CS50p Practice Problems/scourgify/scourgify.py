import sys
import csv


# check for proper sys.argv length
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    pass

before_file = sys.argv[1]
students = []

try:
    with open(before_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            last,first = row["name"].split(", ")
            students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
except FileNotFoundError:
    sys.exit(f"Could not read {before_file}")

with open(sys.argv[2], "w", newline="") as afterfile:
    writer = csv.DictWriter(afterfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
