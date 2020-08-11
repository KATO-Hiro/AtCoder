'''input
2
6 8
3 3
4
1
24 30
7
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    group_count = int(input())

    seated_numbers = [list(map(int, input().split())) for _ in range(group_count)]
    total_person = 0

    for line in seated_numbers:
        total_person += max(line) - min(line) + 1

    print(total_person)
