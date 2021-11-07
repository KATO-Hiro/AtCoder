# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = dict()

    for i in range(n):
        line = list(map(int, input().split()))
        a = tuple(line[1:])

        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    
    print(len(d.keys()))


if __name__ == "__main__":
    main()
