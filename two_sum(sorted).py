#BRUTEFORCE

def target_sum(nums, target):
  if len(nums) < 2:
    return [-1, -1]
  for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums[j] == target:
        return [i,j]
  return [-1, -1]
      

nums = [1,2,3,4,6] 
target = 3
print(target_sum(nums, target))



#OPTIMIZED

def target_sum(nums, target):
    dictt = {}
    for i in range(0,len(nums)):
        if target - nums[i] in dictt:
            return [dictt[target-nums[i]], i]
        dictt[nums[i]] = i
    return [-1,-1]


nums = [1,2,3,4,6] 
target = 3
print(target_sum(nums, target))