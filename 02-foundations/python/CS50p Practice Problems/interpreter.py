x , y , z = input("Expression: ").split()

# Change type of variable x and z
x = float(x)
z = float(z)

# Perform the operations
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
