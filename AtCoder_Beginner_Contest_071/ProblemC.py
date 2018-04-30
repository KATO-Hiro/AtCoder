'''input
5
6 6 6 6 7
36

4
1 2 3 4
0

6
5 5 5 5 6 6
30

6
2 2 3 3 3 3
9

12
3 3 3 3 4 4 4 5 5 5 6 6
30

10
3 3 3 3 4 4 4 5 5 5
20

6
3 1 2 4 2 1
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    n = int(input())
    a = Counter(list(map(int, input().split())))
    sorted_a = sorted(a.items(), key=lambda x: (x[0], x[1]), reverse=True)
    squares = [key for key, value in sorted_a if value >= 4]
    rectangles = [key for key, value in sorted_a if value >= 2]

    if (len(squares) >= 1) and (len(rectangles) >= 2):
        print(max(squares[0] ** 2, rectangles[0] * rectangles[1]))
    elif (len(squares) >= 1) and (len(rectangles) < 2):
        print(squares[0] ** 2)
    elif len(rectangles) >= 2:
        print(rectangles[0] * rectangles[1])
    else:
        print(0)
