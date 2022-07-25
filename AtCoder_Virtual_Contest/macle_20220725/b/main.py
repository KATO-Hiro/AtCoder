# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = Counter()

    for i in range(n):
        s = input().rstrip()
        t = ''.join(sorted(list(s)))
        c[t] += 1
    
    ans = 0

    for key, value in c.items():
        ans += value * (value - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
