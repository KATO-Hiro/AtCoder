# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    ans = inf

    for score in range(101):
        b = a + [score]
        b.sort()
        c = b[1:-1]

        if sum(c) >= x:
            ans = min(ans, score)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
