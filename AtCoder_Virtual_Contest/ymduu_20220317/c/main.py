# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    for i in range(1, n + 1):
        if i in c.keys():
            print(c[i])
        else:
            print(0)


if __name__ == "__main__":
    main()
