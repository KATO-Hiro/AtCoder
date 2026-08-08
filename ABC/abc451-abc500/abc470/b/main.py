# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))
    count = Counter(c)
    freq = count.most_common()[0][1]
    print(n - freq)


if __name__ == "__main__":
    main()
