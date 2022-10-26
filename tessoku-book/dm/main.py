# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for ai in a:
        d[ai % 100] += 1
    
    ans = (d[0] * (d[0] - 1) // 2) + (d[50] * (d[50] - 1) // 2)

    for i in range(1, 50):
        ans += d[i] * d[100 - i]

    print(ans)


if __name__ == "__main__":
    main()
