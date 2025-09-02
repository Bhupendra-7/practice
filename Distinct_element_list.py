# BRUTEFORCE
def CountDist(lst):
    if len(lst) > 1:
        res = 1
        for i in range(1,len(lst)):
            if lst[i] not in lst[0:i]:
                res += 1
        return res
    else:
        return 0

lst = []
print(CountDist(lst))


def CountDist(lst):
    freq = []
    for num in lst:
        if num not in freq:   
            freq.append(num)
    print(len(freq))


# USING SET
lst = [10,20,10,30,30,20] 
res = set(lst) 
print(len(res))


# OPTIMIZED
def CountDist(lst):
    hashmap = {}
    for i in lst:
        if i not in hashmap:
            hashmap[i] = True
    return len(hashmap)

lst = [10,20,10,30,30,20]
print(CountDist(lst))