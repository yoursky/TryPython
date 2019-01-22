
def findSmallest(arr):
    smalllest = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smalllest:
            smalllest = arr[i]
            idx = i
    return idx

def selectSort(arr):
    newArr = []
    # for i in range(len(arr)):
    while arr:
        idx = findSmallest(arr)
        newArr.append(arr.pop(idx))
    return newArr

print selectSort([10, 9, 3, 5])