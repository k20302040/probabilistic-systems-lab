def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    # Length check
    if len(plate) < 2 or len(plate) > 6:
        return False

    # First two must be letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # Only letters and numbers
    if not plate.isalnum():
        return False

    # Numbers rules
    number_started = False
    for char in plate:
        if char.isdigit():
            if not number_started:
                # first number cannot be 0
                if char == "0":
                    return False
                number_started = True
        else:
            # letter after number = invalid
            if number_started:
                return False

    return True





main()
