# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    t = set([input().rstrip() for _ in range(m)])
    count = 0

    for si in s:
        if si[3:] in t:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
