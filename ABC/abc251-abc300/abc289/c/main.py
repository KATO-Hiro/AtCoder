# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list()
    ans = 0

    for _ in range(m):
        ci = int(input())
        ai = list(map(int, input().split()))
        a.append(ai)
    
    patterns = product([0, 1], repeat=m)

    for pattern in patterns:
        s = set()

        for i, p in enumerate(pattern):
            if p == 1:
                for ci in a[i]:
                    s.add(ci)
        
        if len(s) == n:
            ans += 1
    
    print(ans)
    

if __name__ == "__main__":
    main()
