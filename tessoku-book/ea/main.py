# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = Counter(a)
    ans = 0

    for key, value in c.items():
        ans += value * (value - 1) //2

    print(ans)
    

if __name__ == "__main__":
    main()
