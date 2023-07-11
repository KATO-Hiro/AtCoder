# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    size = len(s)
    n = int(input())

    # Tの候補のうち最小値・最大値を考える
    # min: ?を全て0にしたとき、max: 同1にしたとき
    # min > nなら-1
    # そうでなければ、n以下となる場合のみ上の桁から2 ** (n - i)を加算
    t = 0

    for i, si in enumerate(s, 1):
        if si != "?":
            t += 2 ** (size - i) * int(si)

    if t > n:
        print(-1)
    else:
        for i, si in enumerate(s, 1):
            add = 2 ** (size - i)

            if si == "?" and (t + add <= n):
                t += add

        print(t)


if __name__ == "__main__":
    main()
