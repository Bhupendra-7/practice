# BRUTEFORCE
def Remove_Dupl(nums):
    listt = []
    seen = set()
    for i in nums:
        if i not in seen:
            listt.append(i)
            seen.add(i)
    return listt, len(listt)
    

nums = [2, 3, 3, 3, 6, 9, 9]
print(Remove_Dupl(nums))


def Remove_Dupl(nums):
    """
    In-place duplicate removal using pop().
    Time: O(n^2), Space: O(1)
    """
    if len(nums) < 2:
        return len(nums), nums
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)  # remove duplicate, do NOT advance j or else it will skip the incoming elem.
            else:
                j += 1
        i += 1
    return len(nums), nums


# OPTIMIZED
def Remove_Dupl(nums):
    """                                                     
    Efficient in-place using two pointers.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0, []
    slow = 0  # last unique element index
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]  # overwrite next unique position
    return slow + 1, nums[:slow + 1]

"""
nums:  [2, 3, 3, 3, 6, 9, 9]
slow → last unique kept
fast → scanning ahead

When fast finds new unique:
    slow += 1
    nums[slow] = nums[fast]
When fast finds duplicate:
    slow stays
    
If duplicate → fast moves, slow stays.
If unique → slow moves forward, overwrite slow with fast.
"""