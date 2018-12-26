import random
import time


def optimized_bubble_sort(arr):
    """optimized_bubble_sort(arr) --> The optimized approach of bubble sort algorithm which takes less than
    half the run time compared to that of the naive bubble sort algorithm.

    --> Unlike the common bubble sort algorithm that keeps bubbling and swapping from  LEFT to RIGHT, here I keep
    bubbling and swapping on both sides, to the LEFT and to the RIGHT. Even though there is run time improvement, it
    is not good enough to sort millions of items.
    Should I use Parallel Programming like threading or multiprocessing???


    :param arr: Array of integers
    :return: Sorted Array of integers

    """

    j = 0
    while j + 1 < len(arr):
        if arr[j] > arr[j + 1]:
            swap(j, j + 1, arr)
            left_side_sort(arr, j)
        j = j + 1

    return arr



def left_side_sort(arr, j):
    """left_side_sort(arr, j) --> Arranges the left side of the array in sorted order so that our optimized_bubble_sort
                                function avoid the double for loop, unlike the common_bubble_sort function

    :param arr: Array of integers
    :param j: Index of the arr to the right end
    :return:
    """
    while j - 1 >= 0:
        if arr[j] < arr[j - 1]:
            swap(j - 1, j, arr)
            j = j - 1
        else:
            break

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def common_bubble_sort(arr):
    """common_bubble_sort(arr) --> The common approach of bubble sort algorithm optimization

    :param arr: Array of integers
    :return: Sorted Array of integers
    """

    for i in range(len(arr)):
        j = 0
        swapped = False
        while j + 1 < len(arr):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1, arr)
                swapped = True
            j = j + 1
        if swapped == False:
            break
    return arr


arr = []
for x in range(10000):
  arr.append(random.randint(1, 10000))





print(optimized_bubble_sort.__doc__)
start_time = time.time()
for key, value in enumerate(optimized_bubble_sort(arr)):
    print(key + 1, value)
print(optimized_bubble_sort(arr))
print("--- %s seconds ---" % (time.time() - start_time))


# print(common_bubble_sort.__doc__)
# start_time = time.time()
# for key, value in enumerate(common_bubble_sort2(arr)):
#     print(key + 1, value)
# print(common_bubble_sort(arr))
# print("--- %s seconds ---" % (time.time() - start_time))