Python File I/O lets you read, write, and append to files directly from your program. While variables, lists, dicts, etc. get wiped when a program ends, using files lets you keep the data forever. This is useful for large datasets you need to either use or modify. 

Example:
with open("file_name", "r" OR "w" OR "a") as var_name:
    for line in var_name:
        print(line)

In this example, the "with" keyword will automatically close the file when the tasks are completed. 
"open" opens the specified file in a mode of your choosing. 
"r" only lets you read the contents without modifying them. 
"w" rewrites over the entire contents everytime you make a change. 
"a" simply adds content with writing over anything.
var_name will store the contents of the file.
The loop then iterates through var_name line-by-line and prints each line in the terminal.


.txt:
Basic unorganized text file that can store just about anything. Less useful for when you need more organized data.

.csv:
Comma-seperated values.

ID,Name,Role,JoinedDate,Remote
1,Alex Rivera,Manager,2022-01-15,True
2,Sam Chen,Developer,2023-05-10,False
3,Jordan Smith,Designer,2021-11-22,True

The first row is for headers. The rest of the data is organized according to that with each value seperated by a single comma.


There are many other file types.
