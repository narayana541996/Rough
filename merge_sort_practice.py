def merge(arr1, arr2): 
    ai = ai1 = ai2 = 0
    arr = [0] * (len(arr1) + len(arr2))
    while ai1 < len(arr1) and ai2 < len(arr2):
        if arr1[ai1] < arr2[ai2]:
            arr[ai] = arr1[ai1]
            ai1 += 1
        else:
            arr[ai] = arr2[ai2]
            ai2 += 1
        ai += 1

    while ai1 < len(arr1):
        arr[ai] = arr1[ai1]
        ai1 += 1
        ai += 1
    while ai2 <len(arr2):
        arr[ai] = arr2[ai2]
        ai2 += 1
        ai += 1
    return arr
        


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    mergeSort(arr[:mid])
    mergeSort(arr[mid:])
    return merge(arr[:mid], arr[mid:])

print(mergeSort([2,4,1,3]))