import sys
import random
import pyfiglet


if len(sys.argv) == 1:
    input = input("Input: ")
    f = pyfiglet.figlet_format(input, font = random.choice(pyfiglet.FigletFont.getFonts()))
    print(f)
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[2] == "--font":
        input = input("Input: ")
        font = sys.argv[2]
        f = pyfiglet.figlet_format(input, font = font)
        print(f)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
