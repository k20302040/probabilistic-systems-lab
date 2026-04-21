import sys

def main():
    user_input = input("Input: ")
    if user_input.isdigit() == True:
        sys.exit()
    output = f"output: {shorten(user_input)}"
    print(output)

def shorten(user_input):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = user_input

    for char in user_input:
        if char in vowels:
            output = output.replace(char, "")
    return output



if __name__ == "__main__":
    main()

