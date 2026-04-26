import sys

# check for proper sys.argv length
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguements")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguements")
else:
    pass

file_name = sys.argv[1]
# ensure it's actually a py3 file
if file_name[-3:] != ".py":
    sys.exit("Not a Python file")
else:
    pass

file_list = []
try:
    with open(file_name, "r") as file:
        for line in file:
            file_list.append(line)
except FileNotFoundError:
    sys.exit("File does not exist")

lines_count = 0
for line in file_list:
    line = line.strip()
    if line.startswith("#"):
        pass
    elif line == "":
        pass
    else:
        lines_count = lines_count + 1



print(lines_count)
