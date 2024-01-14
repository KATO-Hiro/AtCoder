# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    s = input().rstrip()
    gx, gy = map(int, input().split())
    dir = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    if gx == 0 and gy == 0:
        print("Yes")
        exit()

    for d in permutations(["L", "R", "U", "D"], 4):
        pattern = {"W": dir[d[0]], "X": dir[d[1]], "Y": dir[d[2]], "Z": dir[d[3]]}
        cur_x, cur_y = 0, 0

        for si in s:
            dx, dy = pattern[si]
            cur_x += dx
            cur_y += dy

            if cur_x == gx and cur_y == gy:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
