def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    if "$" in d:
        new_d = d.replace("$", "")
        new_d_flt = float(new_d)
        return new_d_flt


def percent_to_float(p):
    if "%" in p:
        new_p = p.replace("%", "")
        new_p_flt = float(new_p)
        return new_p_flt * 0.01


main()
