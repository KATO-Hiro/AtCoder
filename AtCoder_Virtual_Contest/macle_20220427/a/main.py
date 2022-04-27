# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter()

    for ai in a:
        c[ai % 200] += 1
    
    ans = 0
    
    for value in c.values():
        ans += value * (value - 1) // 2
    
    print(ans)


if __name__ == "__main__":
    main()
