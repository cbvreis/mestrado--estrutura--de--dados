import numpy as np

def merge(a,left,right):
    cont = i = j = 0
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            a[cont] = left[i]
            i += 1
        else:
            a[cont] = right[j]
            j += 1
        cont += 1

    while (i < len(left)):
        a[cont] = left[i]
        i += 1
        cont += 1

    while (j < len(right)):
        a[cont] = right[j]
        cont += 1
        j += 1
    return


def merge_sort(a):
    if len(a) >1:
        q = (len(a) // 2)
        left=a[:q]
        right=a[q:]
        merge_sort(left)
        merge_sort(right)
        merge(a,left,right)
    else:
        return


vector = np.random.randint(0, 9999, 72000)
merge_sort(vector)
print(vector)