# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    t = list(map(int, input().split()))
    d = dict()

    for _ in range(m):
        si, ci = map(int, input().split())

        if si not in d.keys():
            d[si] = ci
        else:
            d[si] = min(d[si], ci)

    ans = 0

    for ti in t:
        if ti not in d.keys():
            print(-1)
            exit()

        ans += d[ti]

    print(ans)


if __name__ == "__main__":
    main()
