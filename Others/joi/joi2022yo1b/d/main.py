# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = Counter(list(map(int, input().split())))

    print(sorted(a.items(), key=lambda x: (x[1], x[0]))[0][0])


if __name__ == "__main__":
    main()
