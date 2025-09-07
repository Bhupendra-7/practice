# BEST
def Rev(arr):
    if len(arr) <= 1:
        return arr
    i = 0
    j = len(arr) - 1
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]  # swap
        i += 1
        j -= 1  
    return arr


#USING LIST
def Rev(arr):
    if len(arr) <= 1:
        return arr
    lst = []
    for i in range(len(arr)-1, -1, -1):
        lst.append(arr[i])
    return lst


#ONE LINER
def Rev(arr):
    return arr[::-1]

