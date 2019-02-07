""" QUESTION 5
Use lambda and print the square of all even numbers in the range (1 – 100)

"""


def square_of_all_evens():

    # return [e**2 for e in range(101) if e % 2 == 0]
    evens = filter(lambda e: e % 2 == 0, [i for i in range(1, 101)])
    return [e**2 for e in evens]

print(square_of_all_evens())