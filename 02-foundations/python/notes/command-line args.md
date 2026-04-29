An alternative to input(). Lets you get user input directly from the command line.
Example:

*CODE*

import sys
user_input = sys.argv[1]
print(user_input)
-------------------------------------
*TERMINAL*
                  |---| 
> python hello.py John

