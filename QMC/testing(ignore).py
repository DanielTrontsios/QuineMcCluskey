# test = []
# x = int(input("What is x?"))
#
# test.append('x' if x == 1 else '-')
#
# print(test)

# from itertools import combinations
#
# test = [1,2,3,4]
#
# for i in combinations(test, 3):
#     print(i)

# string = "1,2,3,4,5,6"
# ls = []
#
# for i in string.split(','):
#     ls.append(int(i))
#
# print(ls)

test = [[8, 9, 10, 11], [8, 10, 12, 14], [10, 11, 14, 15]]
tm = [4, 8, 10, 11, 12, 15]
result = []

for matches in test:
    result.append([])
    for i in tm:
        if i in matches:
            result[-1].append('x')
        else:
            result[-1].append('-')

print(result)