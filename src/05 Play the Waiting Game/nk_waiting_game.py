import random
from time import time


def waiting_game():
    wait_time = random.randint(1, 4)
    print("Your target time is " + str(wait_time) + " seconds.")
    input(print("---Press Enter to Begin---"))
    t_start = time()

    input(print("...Press Enter again after " + str(wait_time) + " seconds..."))
    t_diff = time() - t_start

    print("Elapsed time: " + str(t_diff) + " seconds")
    if t_diff > wait_time:
        return print("(" + str(t_diff - wait_time) + " seconds too slow)")
    elif t_diff < wait_time:
        return print("(" + str(wait_time - t_diff) + " seconds too fast)")
    else:
        return print("Exactly on target!")
