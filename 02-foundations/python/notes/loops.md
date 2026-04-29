## Loops allow you to repeat a certain task or chunk of code however many times you want.

### Instead of:
    print("Meow")
    print("Meow")
    print("Meow")
    print("Meow")
    print("Meow")

### Do:
    for i in range(5):
        print("meow")


### Saves time and space.


## while loops continue for as long as the conditional is True:

    i = 0
    while i < 3:
        print("meow")
        i += 1
    
### The value of "i" will increase each time until it hits 3. Then the loop breaks.

## for loops:
    for i in range(5):
        print("meow")
    
### Allows you to iterate through objects, such as lists.
