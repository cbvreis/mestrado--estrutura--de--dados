import numpy as np


def insertion_sort(a):
    troca = i = key = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            troca = troca + 1
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    print(troca)
    return a

vector = np.random.randint(0, 9999, 72000)
print(vector)
print(insertion_sort(vector))
