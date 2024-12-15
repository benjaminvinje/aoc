# read file
txt_day1 = open("day1.txt", "r")
content = txt_day1.read()


"""
part 1 
"""
# make a list of each number in content
lst = [int(x) for x in content.split()]
# take from 0 position and pick pr. second - sorted
left = sorted(lst[0::2])
# take from 1 position and pr. second - sorted
right = sorted(lst[1::2])

# sum of absolute distance for each element in left and right pair
hygge = sum([abs(a - b) for a, b in zip(left, right)])


"""
part 2 
"""

from collections import Counter

count = Counter(right)
for x in left:
    gange = (x * count[x] for x in left)
    result = sum(gange)
print(result)











    



