# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, d, p = map(int, input().split())
    f = sorted(list(map(int, input().split())), reverse=True)
    total = sum(f)
    ans = min(total, ceil(n / d) * p)

    for i, fi in enumerate(f):
        if i % d == 0:
            ans = min(ans, total)
            total += p

        total -= fi

    print(ans)


if __name__ == "__main__":
    main()
