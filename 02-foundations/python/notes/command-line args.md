## An alternative to input(). Lets you get user input directly from the command line.
## Example:

### CODE
import sys
print(f"Hello, {sys.argv[1]}")

### TERMINAL
> python hello.py John
> Hello John


## First import "sys". This gives you access to command-line arguments. The arguements are 0-indexed, starting with the file name. You can then access the arguments with ".argv([index])". 
