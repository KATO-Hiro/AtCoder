'''input
5 3
###
..#
###
#..
###
Impossible

4 5
##...
.###.
.###.
...##
Impossible

4 5
##...
.##..
..##.
...##
Possible

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    h, w = list(map(int, input().split()))
    board = [input() for i in range(h)]
    count = sum([board[i].count('#') for i in range(h)])

    # See:
    # https://www.youtube.com/watch?v=6ZP8JyGsQBs
    if count == (h + w - 1):
        print('Possible')
    else:
        print('Impossible')
