# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for key, value in c.items():
        if value % 2 == 0:
            continue

        ans += key

    print(ans)


if __name__ == "__main__":
    main()
