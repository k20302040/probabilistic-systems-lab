def main():
    time = input("What time is it? ")
    flt_time = convert(time)

    if 8 >= flt_time >= 7:
        print("breakfast time")
    elif 13 >= flt_time >= 12:
        print("lunch time")
    elif 19 >= flt_time >= 18:
        print("dinner time")


def convert(time):
    hrs, uncalculated_mins = time.split(":")
    mins = float(uncalculated_mins) / 60
    flt_time = float(hrs) + mins
    return flt_time



if __name__ == "__main__":
    main()
