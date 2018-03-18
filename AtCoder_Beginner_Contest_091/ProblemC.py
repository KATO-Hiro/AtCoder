'''input
5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7

5

5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9

4

2
2 2
3 3
0 0
1 1

0

3
2 0
3 1
1 3
4 2
0 4
5 5

2

3
0 0
1 1
5 2
2 3
3 4
4 5

2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def get_candidate_points(sorted_a_b: list, c: int, d: int) -> list:
    candidate_a_b = [x for x in sorted_a_b if (x[0] < c) and (x[1] < d)]
    return sorted(candidate_a_b, key=lambda x: (x[1], x[0]), reverse=True)


if __name__ == '__main__':
    number = int(input())

    a_b = [list(map(int, input().split())) for _ in range(number)]
    c_d = [list(map(int, input().split())) for _ in range(number)]
    sorted_a_b = sorted(a_b, key=lambda x: (x[0], x[1]))
    sorted_c_d = sorted(c_d, key=lambda y: (y[0], y[1]))
    count = 0

    for c, d in sorted_c_d:
        points = get_candidate_points(sorted_a_b, c, d)

        if len(points) >= 1:
            sorted_a_b.remove(points[0])
            count += 1

    print(count)
