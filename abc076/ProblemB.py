'''input
10
10
76
4
3
10
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    operation_count = int(input())
    incremental_value = int(input())
    candidates = list()

    for i in range(operation_count + 1):
        result = 2 ** i + (operation_count - i) * incremental_value
        candidates.append(result)

    print(min(candidates))
