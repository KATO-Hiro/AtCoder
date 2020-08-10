'''input
2 2
6

5 15
1


'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    k, s = list(map(int, input().split()))
    count = 0

    for x in range(k + 1):
        for y in range(k + 1):
            z = s - (x + y)

            if 0 <= z <= k:
                count += 1

    print(count)
