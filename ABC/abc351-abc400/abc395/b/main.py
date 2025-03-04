# -*- coding: utf-8 -*-

from typing import List


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: List[List]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [["." for _ in range(n)] for _ in range(n)]

    for _ in range(4):
        for i in range(n):
            for j in range(i, n - i):
                if i > j:
                    continue

                if i % 2 == 0:
                    ans[i][j] = "#"

        ans = rotate_90_degrees_to_right(ans)

    for ans_i in ans:
        print("".join(ans_i))


if __name__ == "__main__":
    main()
