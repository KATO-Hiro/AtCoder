# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**20
    ans = inf

    for ai in a:
        p, q = divmod(t, ai)

        if q == 0:
            ans = min(ans, t)
        else:
            ans = min(ans, t + (ai - q))

    print(ans)


if __name__ == "__main__":
    main()
