"""
5. Reverse a given string (don’t use inbuilt methods)

"""
def reverse(string):
    return "".join(string[i] for i in range(len(string)-1, -1, -1))



print(reverse("string"))
print(reverse("reversing"))