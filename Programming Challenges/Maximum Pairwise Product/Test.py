import collections
from itertools import count

def get_nth_index(lst, item, n):
    c = count(1)
    return next((i for i, x in enumerate(lst) if x == item and next(c) == n), None)

a = [9,8,2,3,8,3,5,8,9,9,9]

duplicates_list = [item for item, count in collections.Counter(a).items() if count > 1]
print(duplicates_list)


for dup_num in duplicates_list:
    indx = get_nth_index(a, dup_num, 2)
    if indx is not None:
        del a[indx]

print(a)
# [9, 8, 2, 3,
