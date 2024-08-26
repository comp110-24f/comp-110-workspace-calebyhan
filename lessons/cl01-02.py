# bubble sort

import random
import time


def bubble(n: int) -> tuple[list[float], int]:
    a = [random.random() for _ in range(n)]

    iter = 0

    for i in range(len(a)):
        done = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                done = True
            iter += 1
        if not done:
            break

    return a, iter


n = 10000
iter_sum = 0
time_sum = 0

for i in range(n):
    start = time.time()
    lst, iter = bubble(100)
    time_sum += time.time() - start
    assert lst == sorted(lst), "not correct"
    iter_sum += iter

print(f"Average iterations: {iter_sum / n}")
print(f"Average time: {time_sum / n}")
