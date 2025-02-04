# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    b = [[] for _ in range(w)]

    for i in range(n):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        b[xi].append((i, yi))

    inf = 10**18
    size_min = inf

    for bi in b:
        size_min = min(size_min, len(bi))

    # ブロックが消失する最小の時間
    t = [inf] * n

    for row in range(size_min):
        t_max = 0

        for col in range(w):
            _, ti = b[col][row]
            t_max = max(t_max, ti)

        for col in range(w):
            pos, _ = b[col][row]
            t[pos] = t_max + 1

    q = int(input())

    for _ in range(q):
        ti, ai = map(int, input().split())
        ai -= 1

        tj = t[ai]

        if ti < tj:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
