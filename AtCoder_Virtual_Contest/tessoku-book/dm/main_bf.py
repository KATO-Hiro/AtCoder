# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = set()

    for x, ax in enumerate(a):
        for y, ay in enumerate(a):
            if x >= y:
                continue

            if (ax + ay) % 100 == 0:
                ans.add((x, y))

    print(len(ans))


if __name__ == "__main__":
    main()
