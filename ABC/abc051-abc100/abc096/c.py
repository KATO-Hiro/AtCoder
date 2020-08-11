'''input
5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#
No

11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##.
Yes

3 3
.#.
###
.#.
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    h, w = list(map(int, input().split()))
    board = [list(map(str, input())) for _ in range(h)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#':
                count = 0

                for k in range(len(dx)):
                    x = i + dx[k]
                    y = j + dy[k]

                    if (x >= 0) and (x < h) and (y >= 0) and (y < w) and (board[x][y] == "#"):
                        count += 1

                if count == 0:
                    print('No')
                    exit()

    print('Yes')
