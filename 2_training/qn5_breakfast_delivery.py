#!/usr/bin/env python3
import random

from collections import Counter
def get_lost_drones(lst):
    """get_lost_drones(lst) --> function receiving a list of drone's unique id which was collected when the drone
     went out for delivery and come back from delivery.

    ---> This function is a little bit more generalized version of the question as it will output the unique ids of all
    the lost drones, not only just one lost drone unique id.

    :param lst: Array of integers
    :return:
    """


    counter = Counter(lst)
    # print(counter)
    lost_drones = []
    for key in counter:
        if counter[key] % 2 != 0:
            lost_drones.append(key)
    return lost_drones

if __name__ == "__main__":
    delivery_id_confirmations = [1, 2, 3, 4, 2, 3, 4, 1, 5, 9, 9, 9, 9, 44, 44, 88, 88, 100, 100, 100, 100, 100, 100]
    print("The lost drone id is {}".format(get_lost_drones(delivery_id_confirmations)))

    arr = []
    for x in range(100):
        arr.append(random.randint(1, 101))
    # print(arr)
    print("All the lost drones ids are listed here {}".format(get_lost_drones(arr)))

