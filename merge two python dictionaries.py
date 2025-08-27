def merge(dict1, dict2):
  dict1.update(dict2)
  return dict1

dict1 = {'a':1, 'b':2, 'c': 3}
dict2 = {'d':4, 'e':7}
print(merge(dict1, dict2))


#WITH LOOP
def merge(dict1, dict2):
  for i in dict2:
    if i not in dict1:
      dict1[i] = dict2[i]
  return dict1
    
dict1 = {'a':1, 'b':2, 'c': 3}
dict2 = {'d':4, 'e':7}
print(merge(dict1, dict2))


#UNPACKING
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 7}

merged = {**dict1, **dict2}
print(merged)
"""
**unpacks the key-value pairs from each dictionary into a new dictionary.
Original dictionaries remain unchanged.
"""

