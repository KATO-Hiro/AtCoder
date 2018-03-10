'''input
64145 123 456
109
13 3 1
3
12 3 1
2
100000 1 1
49999
64146 123 456
110
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    total_width, width_per_person, span = list(map(int, input().split()))

    result = (total_width - span) // (width_per_person + span)
    print(result)
