'''input
2 4
No

1 3
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    x, y = map(int, input().split())

    groupA = [1, 3, 5, 7, 8, 10, 12]
    groupB = [4, 6, 9, 11]
    groupC = [2]

    condition1 = (x in groupA) and (y in groupA)
    condition2 = (x in groupB) and (y in groupB)
    condition3 = (x in groupC) and (y in groupC)

    if condition1 or condition2 or condition3:
        print('Yes')
    else:
        print('No')
