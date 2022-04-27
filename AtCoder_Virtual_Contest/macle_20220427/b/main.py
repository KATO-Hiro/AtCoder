# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    total = 0

    for value in c.values():
        total += value * (value - 1) // 2
    
    for ai in a:
        count = c[ai]
        tmp = total
        tmp -= count * (count - 1) // 2
        tmp += (count - 1) * (count - 2) // 2
        print(tmp)


if __name__ == "__main__":
    main()
