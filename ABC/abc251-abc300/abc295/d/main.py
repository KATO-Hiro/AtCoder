# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    b = 0
    c = Counter()
    c[b] += 1

    for si in s:
        b = b ^ (1 << int(si))
        c[b] += 1
    
    ans = 0
    
    for value in c.values():
        ans += value * (value - 1) // 2
    
    print(ans)
    

if __name__ == "__main__":
    main()
