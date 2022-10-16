# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(sorted(a, reverse=True))
    ans = [0] * n

    for i, value in enumerate(c.values()):
        ans[i] = value
    
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
