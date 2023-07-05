# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    color_id = 0
    ans = [[0 for _ in range(w)] for _ in range(h)]

    # 構築: 列方向に順番に配置すると良さそう
    for row in range(h):
        if row % 2 == 0:
            r = range(w)
        else:
            r = range(w - 1, -1, -1)

        for col in r:
            ans[row][col] = color_id + 1
            a[color_id] -= 1

            if a[color_id] == 0:
                color_id += 1

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
