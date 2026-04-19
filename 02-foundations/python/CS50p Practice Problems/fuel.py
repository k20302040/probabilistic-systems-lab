def main():
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
    except:
        main()
    decimal = fraction_to_decimal(x, y)
    percent = decimal_to_percent(decimal)
    print(percent)

def fraction_to_decimal(x, y):
    try:
        decimal = int(x)/int(y)
        if decimal > 1:
            main()
        else:
            return round(decimal, 2)
    except ValueError:
        main()
    except ZeroDivisionError:
        main()

def decimal_to_percent(decimal):
    percent = int(decimal * 100)
    if percent > 100 or percent < 0:
        main()
    elif percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    percent = str(percent)
    return percent + "%"


main()
