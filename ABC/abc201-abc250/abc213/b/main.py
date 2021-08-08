# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list()

    for index, ai in enumerate(a, 1):
        b.append((ai, index))
    
    sorted_b = sorted(b)
    print(sorted_b[-2][1])


if __name__ == "__main__":
    main()
