# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    l = [0] + list(accumulate(l))
    ans = 0

    for li in l:
        if 0 <= li <= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
