
def print_inreverse(string):
    if string == "":
        return
    print_inreverse(string[1:])
    print(string[0])

print_inreverse("abcdefgh")

def print_normally(string):
    if string == "":
        return
    print(string[0])
    print_normally(string[1:])

print("----------")
print_normally("abcdefgh")

def recursive_three(string):
    string = list(string)
    return foo_three(string, 0, len(string) - 1)

def foo_three(string, i, j):
    if i >= j:
        return string
    string[i], string[j] = string[j], string[i]
    return foo_three(string, i + 1, j - 1)

print(recursive_three("abcdefghijklmnopqrstuvwxyz"))