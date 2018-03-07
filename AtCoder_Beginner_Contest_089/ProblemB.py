'''input
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    arare_count = int(input())
    arares = list(map(str, input().split(" ")))

    if len(set(arares)) == 3:
        print("Three")
    elif len(set(arares)) == 4:
        print("Four")
