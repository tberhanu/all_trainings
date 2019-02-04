"""
3. Return True if all the letters are unique
"""

def is_all_letters_unique(string):

    """ Code I """
    # for i, s in enumerate(string):
    #     if s in string[:i] or s in string[i+1:]:
    #         return False
    # return True

    """ Code II """
    return not any(99 for i, s in enumerate(string) if s in string[:i] or s in string[i+1:])



print(is_all_letters_unique("string"))
print(is_all_letters_unique("stringedef"))