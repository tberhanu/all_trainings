def input(n):
    try :
        assert (n in range(-5, 6)), "The input is out of the expected range"
        return True
    except AssertionError as e:
        return e


for i in range(-7, 8):
    print(input(i))