def qsort(a):
    if len(a) < 2:
        return a
    pivot = a[0]
    less = [i for i in a[1:] if i <= pivot]
    great = [i for i in a[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(great)

print qsort([10, 5, 2, 3])