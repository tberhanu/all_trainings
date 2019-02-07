""" QUESTION 3"""

def is_prime(num):
    if num == 2:
        return True
    elif num <= 1 or num % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i = i + 2
        return True


for num in range(101, 1001, 2):
    if is_prime(num):
        print(num)


        