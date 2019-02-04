"""
4. Remove duplicates of arr or string
"""
def remove_duplicates(string):


    """ Code I"""
    # dict = {}
    # arr = [dict.setdefault(s,s) for s in string if s not in dict]
    # return "".join(arr)

    """ Code II """
    return "".join(list(set(string)))



print(remove_duplicates("fabcabbcdeff"))