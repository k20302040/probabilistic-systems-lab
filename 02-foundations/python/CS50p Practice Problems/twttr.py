input = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
output = input

for char in input:
    if char in vowels:
        output = output.replace(char, "")


print(f"output: {output}")
