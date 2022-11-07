# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    
    for i in range(1, n + 1):
        print(m - c[i])


if __name__ == "__main__":
    main()
