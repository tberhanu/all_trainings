def get_substring_index(string, substring):
    if substring not in string:
        return -1
    else:
        return string.index(substring)


string = "hello"
sub = "ello"
print(get_substring_index(string, sub))
string = "hello"
sub = "llo"
print(get_substring_index(string, sub))
string = "hello"
sub = "o"
print(get_substring_index(string, sub))
