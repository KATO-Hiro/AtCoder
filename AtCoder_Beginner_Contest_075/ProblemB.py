'''input
3 5
#####
#####
#####

#####
#####
#####

3 5
.....
.#.#.
.....

11211
1#2#1
11211

6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...

#####3
#8#7##
####5#
4#65#2
#5##21
#4#310

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


def is_filled_with_all_bombs(s, height, width):
    bomb_count = 0

    for i in range(height):
        bomb_count += s[i][0].count('#')

    return bomb_count == height * width


def replace_dot_with_number(s, height: int, width: int) -> list:
    results = list()
    mod_s = ''

    for i in range(height):
        for j in range(width):
            if s[i][0][j] == '.':
                bomb_count = count_bombs_in_eigth_cells(s, i, j)
                mod_s += str(bomb_count)
            else:
                mod_s += '#'
        results.append(mod_s)
        mod_s = ''

    return results


def count_bombs_in_eigth_cells(s, x: int, y: int) -> int:
    count = 0
    height = len(s)
    width = len(s[0][0])

    for i in range(x - 1, x + 2):
        if (i == x - 1 < 0):
            continue
        if (i == x + 1 > height - 1):
            continue
        for j in range(y - 1, y + 2):
            if (j == y - 1 < 0):
                continue
            if (j == y + 1 > width - 1):
                continue

            if s[i][0][j] == '#':
                count += 1
    return count


def output(results):
    for line in results:
        print(''.join(line))


if __name__ == '__main__':
    height, width = list(map(int, input().split()))
    s = [list(map(str, input().split())) for _ in range(height)]

    if is_filled_with_all_bombs(s, height, width):
        output(s)
    else:
        results = replace_dot_with_number(s, height, width)
        output(results)
