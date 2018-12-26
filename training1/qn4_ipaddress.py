def increment_ip():
    """increment_ip() --> increment ip address starting from 10.10.10.1 up to 10.11.255.255

    :return: Array of Strings
    """
    s1 = "10.10.10."
    s2 = "10.10."
    last = "10.11.255.255"
    arr1 = []
    arr2 = []
    for i in range(255):
        if i >= 10:
            arr2.append(s2 + str(i + 1) + ".255")
        arr1.append(s1 + str(i + 1))
    arr2.append(last)
    return arr1 + arr2

# print(increment_ip.__doc__)
array = increment_ip()
# print(array)

for a in array:
    print(a)