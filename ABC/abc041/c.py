'''input
8
3 1 4 15 9 2 6 5
4
5
7
8
3
1
6
2

3
140 180 160
2
3
1

2
1000000000 1
1
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    order = [int(i) for i in range(1, n + 1)]
    a = list(map(int, input().split()))
    a_dict = {int(key): value for key, value in enumerate(a, 1)}
    sorted_dict = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)

    for index, height in sorted_dict:
        print(index)
