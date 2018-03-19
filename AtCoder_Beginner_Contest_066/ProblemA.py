'''input
700 600 780

1300

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    bells = list(map(int, input().split()))
    bells.sort()

    print(sum(bells[:2]))
