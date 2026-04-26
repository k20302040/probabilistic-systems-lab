import sys
import csv
import tabulate

# check for proper sys.argv length
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguements")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguements")
else:
    pass

file_name = sys.argv[1]
# ensure it's actually a py3 file
if file_name[-4:] != ".csv":
    sys.exit("Not a Python file")
else:
    pass


with open(file_name, mode='r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

print(tabulate.tabulate(data, headers="firstrow", tablefmt="grid"))
