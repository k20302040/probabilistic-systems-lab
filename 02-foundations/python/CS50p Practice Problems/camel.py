input = input("camelCase: ")
output = input

for char in input:
    if char.isupper() == True:
        output = output.replace(char, f"_{char.lower()}")
    else:
        None

print(f"snake_case: {output}")
