amount_due = 50

while True:
    print(f"Amount due: {amount_due}")
    insert_coin = int(input("Insert coin: "))

    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_due = amount_due - insert_coin
    if amount_due < 0:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")
        break
    if amount_due == 0:
        print(f"Change Owed: 0")
        break
