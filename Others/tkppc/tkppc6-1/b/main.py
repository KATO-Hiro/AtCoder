# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    ans = len(a.keys())
    remain = m

    for key, value in a.items():
        if remain > 0 and value > 1:
            count = min(remain, value - 1)
            remain -= count
            ans += count

    print(ans)


if __name__ == "__main__":
    main()
