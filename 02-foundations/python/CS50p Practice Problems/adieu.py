import inflect
inflct = inflect.engine()

names = []

while True:
    try:
        new_name = input("Name: ")
        names.append(new_name)
    except EOFError:
        print()
        output = inflct.join(names)
        print("Adieu, adieu, to" + " " + output)
        raise SystemExit
