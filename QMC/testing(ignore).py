# test = []
# x = int(input("What is x?"))
#
# test.append('x' if x == 1 else '-')
#
# print(test)

from itertools import combinations

test = [1,2,3,4]

for i in combinations(test, 3):
    print(i)