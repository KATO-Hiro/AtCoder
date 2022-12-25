# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    ans = 0
    
    for a, b in combinations(range(n), 2):
        count = 0

        for sa, sb in zip(s[a], s[b]):
            if sa == "o" or sb == "o":
                count += 1
    
        if count == m:
            ans += 1
    
    print(ans)
    

if __name__ == "__main__":
    main()
