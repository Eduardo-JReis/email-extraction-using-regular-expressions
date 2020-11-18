# Importing modules required for regular expressions
import re

# Opening a text file
# and assign it to a file object variable
fhand = open("email_text_file.txt", "r")

for line in fhand:
    # getting the text file content line by line
    s = line.strip()

    # regex for extracting all email-ids from the text file
    reg = re.findall(r"[A-Za-z0-9._%+-]+"
                    r"@[A-Za-z0-9.-]+"
                    r"\.[A-Za-z]{2,4}", s)

    
    # printing the output
    print(reg)