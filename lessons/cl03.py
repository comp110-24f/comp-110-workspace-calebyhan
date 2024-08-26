# selection sort

import random
import time


def selection(n: int) -> tuple[list[float], int]:
    a = [random.random() for _ in range(n)]

    ret = []
    iter = 0

    for _ in range(len(a)):
        least = 0
        for j in range(len(a)):
            if a[least] > a[j]:
                least = j
            iter += 1
        ret.append(a[least])
        a.pop(least)

    return a, iter


n = 10000
iter_sum = 0
time_sum = 0

for i in range(n):
    start = time.time()
    lst, iter = selection(100)
    time_sum += time.time() - start
    assert lst == sorted(lst), "not correct"
    iter_sum += iter

print(f"Average iterations: {iter_sum / n}")
print(f"Average time: {time_sum / n}")
