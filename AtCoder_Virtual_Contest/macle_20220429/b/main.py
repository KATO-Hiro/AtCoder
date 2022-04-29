# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    summed = 0

    for value in c.values():
        summed += value * (value - 1) // 2
    
    for ai in a:
        tmp = summed
        value = c[ai]
        tmp -= value * (value - 1) // 2
        tmp += (value - 1) * (value - 2) // 2
        print(tmp)


if __name__ == "__main__":
    main()
