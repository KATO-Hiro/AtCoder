'''input
8
3 1 4 1 5 9 2 6
8

4
2 3 7 9
7

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    house_count = int(input())
    coordinates = list(map(int, input().split()))
    print(max(coordinates) - min(coordinates))
