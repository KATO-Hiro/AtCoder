# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = Counter(a)

    for _ in range(m):
        bj, cj = map(int, input().split())
        d[cj] += bj

    ans = 0

    for key in sorted(d.keys(), reverse=True):
        count = min(n, d[key])
        ans += count * key

        n -= count

        if n == 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
