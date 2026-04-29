## Exception - something that goes wrong in a program and doesn't let it run.

### try & except lets you catch errors before the user sees them and gives you the option of not having to end the program immediately in case one happens:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")


### If you want nothing to happen in the case of an exception but still need to put something down for syntaz purposes, use "pass"

### Catching exceptions adds more depth to programs and lets you be more creative with your logic.
