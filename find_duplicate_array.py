#BRUTEFORCE
def Find_Dup(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


#OPTIMIZED
def Find_Dup(arr):
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    for j in arr:
        if hash[j] >= 2:
            return j
    return -1


# USING SET
def Dup(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return -1



arr = [1, 3, 4, 2, 2]
print(Find_Dup(arr))