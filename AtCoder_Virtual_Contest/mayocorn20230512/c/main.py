# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = Counter(a)
    ans = 0

    for key, value in c.items():
        if value % 2 == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
