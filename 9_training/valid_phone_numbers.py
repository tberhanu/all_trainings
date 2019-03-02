"""Given a text file file.txt that contains list of phone numbers (one per line), write a one
liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats:
(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
"""

def valid_phone_numbers():
    import re
    arr = []
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}|\d{3}\s\d{3}\s\s{4}|\(\d{3}\)\s\d{3}-\d{4}')
    with open("file.txt", 'r') as f:
        for line in f:
            matches = pattern.findall(line)
            if matches:
                arr.extend(matches)

    return arr

print(valid_phone_numbers())



