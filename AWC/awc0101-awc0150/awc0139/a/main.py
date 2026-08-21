# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for key in c:
        if key == 0:
            continue

        if c[key] <= c[0]:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
