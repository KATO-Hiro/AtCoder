# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    ans = min(len(a.keys()) + m, n)
    print(ans)


if __name__ == "__main__":
    main()
