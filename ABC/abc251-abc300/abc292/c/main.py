# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    ans = 0

    for a in range(1, n):
        for b in range(1, n):
            if a * b > n:
                break

            d[a * b] += 1
    
    for ab in range(1, n):
        cd = n - ab
        ans += d[ab] * d[cd]
    
    print(ans)
    

if __name__ == "__main__":
    main()
