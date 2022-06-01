# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = Counter(a)
    q = int(input())
    ans = sum(a)

    for i in range(q):
        bi, ci = map(int, input().split())

        if bi not in d.keys() or d[bi] == 0:
            print(ans)
            continue

        d[ci] += d[bi]
        ans += (ci - bi) * d[bi]
        d[bi] = 0
        print(ans)


if __name__ == "__main__":
    main()
