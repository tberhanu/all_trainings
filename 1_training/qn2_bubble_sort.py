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
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            j = j + 1
        if swapped == False:
            break
    return arr

def optimized_bubble_sort(arr):
    """
    Here basically we keep track of the last index where we did swapping which tell us
    everything after that index is already sorted so no need to repeat the process of
    comparison. Therefore, every loop, we decrement our second loop range, n, depending
    where the last swap happened.
    """
    n = len(arr)
    swap = False
    while n > 1:
        for j in range(1, n, 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]
                last_swap_index = j
                swap = True
        if swap:
            n = last_swap_index
            swap = False

        else:
            break
    return arr

import random
import time
if __name__ == "__main__":
    arr = []
    for x in range(100):
      arr.append(random.randint(1, 100))





    start_time = time.time()
    for key, value in enumerate(common_bubble_sort(arr)):
        print(key + 1, value)
    print(common_bubble_sort(arr))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for key, value in enumerate(optimized_bubble_sort(arr)):
        print(key + 1, value)
    print(optimized_bubble_sort(arr))
    print("--- %s seconds ---" % (time.time() - start_time))
