grocery_list = {}

while True:
    try:
        item = input()
        item = item.upper()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1

    except EOFError:
        sorted_grocery_list = dict(sorted(grocery_list.items()))
        for key, value in sorted_grocery_list.items():
            print(f"{value} {key}")


        break
