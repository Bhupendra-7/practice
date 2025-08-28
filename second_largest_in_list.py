import math
def sec_lar(lst):
  maxx = -math.inf
  sec_maxx = -math.inf
  
  if len(lst) < 2:
    return None
  for i in lst:
    if i > maxx:
      sec_maxx = maxx
      maxx = i
    elif i != maxx and i > sec_maxx:
      sec_maxx = i
  if sec_maxx == -math.inf:
      return None
  return sec_maxx
      

lst = [2,12,9,7,16]
print(sec_lar(lst))


#SORTING/for distinct elements
lst = [2,12,9,7,16]
lst.sort()
print(lst[-2])