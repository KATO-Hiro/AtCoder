# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 10**18

    for i in range(1, 9):
        ans = min(ans, c[i])

    print(ans)


if __name__ == "__main__":
    main()
