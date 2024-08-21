# bubble sort

a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

for i in range(len(a)):
    done = False
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            done = True
    if not done:
        break

print(a)
