# -*- coding: utf-8 -*-


def mex(x, y, z):
    used = [False] * 4

    for i in [x, y, z]:
        used[i] = True

    for i, u in enumerate(used):
        if not u:
            return i


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    s = input().rstrip()

    # SiとAiの組み合わせは9種類
    # 言い換え: 列Xから(連続とは限らない)部分列Yとなる場合の得点の合計
    # dp
    dp_m = [0] * 3
    dp_e = [[0 for _ in range(3)] for _ in range(3)]
    ans = 0

    for ai, si in zip(a, s):
        if si == "M":
            dp_m[ai] += 1
        elif si == "E":
            for i in range(3):
                dp_e[ai][i] += dp_m[i]
        else:
            for x in range(3):
                for y in range(3):
                    ans += dp_e[x][y] * mex(x, y, ai)
                    pass

    print(ans)


if __name__ == "__main__":
    main()
