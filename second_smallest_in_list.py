def second_smallest(lst):
  smallest = float("inf")
  sec_smallest = float("inf")
  
  for i in lst:
    if i < smallest:
      sec_smallest = smallest
      smallest = i
    elif i > smallest and i < sec_smallest:
      sec_smallest = i
  if sec_smallest == float("inf"):
    return None

  return sec_smallest
      
    
lst = [2,662,2,12]
print(second_smallest(lst))